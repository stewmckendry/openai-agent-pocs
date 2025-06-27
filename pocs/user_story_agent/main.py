"""Entry point for the User Story Agent PoC.

Requirements:
- Place any feature description text in ``test/sample_input.txt`` to try
  the canned example.
- Run with ``python -m pocs.user_story_agent.main`` and enter your own
  feature description or pipe the file as stdin.
"""

import argparse
import asyncio
import os
from pathlib import Path
from datetime import datetime

from agents import gen_trace_id, trace
from agents.exceptions import InputGuardrailTripwireTriggered
from agents.mcp import MCPServerStdio

from agents.extensions.models.litellm_model import LitellmModel
import litellm
litellm.drop_params = True
from .deliverylead import DeliveryLeadManager, visualize_workflow


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Model to use (e.g. openai/gpt-4o)")
    parser.add_argument("--api-key", type=str, help="API key for the model")
    args = parser.parse_args()

    model_name = args.model if args.model else os.environ["MODEL"]
    api_key = args.api_key if args.api_key else os.environ["MODEL_API_KEY"]
    model = LitellmModel(model=model_name, api_key=api_key)

    feature = input("Enter a feature description: ")
    context_dir = Path(__file__).resolve().parent / "resources" / "context_files"

    async with MCPServerStdio(
        name="Filesystem Server", 
        params={"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", str(context_dir)]},
    ) as server:
        trace_id = gen_trace_id()
        with trace("user_story_poc", trace_id=trace_id):
            mgr = DeliveryLeadManager(server, model=model)
            try:
                result = await mgr.run(feature, trace_id=trace_id)
            except InputGuardrailTripwireTriggered as exc:
                info = exc.guardrail_result.output.output_info
                print(f"\nInput rejected: {getattr(info, 'reason', '')}")
                return
            print(
                "\nTrace:",
                f"https://platform.openai.com/traces/trace?trace_id={trace_id}\n",
            )

            print("\n--- User Story ---\n")
            print(result.story.story)

            output_dir = Path(__file__).resolve().parent / "outputs"
            output_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            story_file = output_dir / f"story_{timestamp}.md"
            resource_dir = context_dir
            resource_files = [str(p.relative_to(resource_dir)) for p in resource_dir.rglob("*") if p.is_file()]
            with open(story_file, "w", encoding="utf-8") as f:
                f.write("## User:\n")
                f.write(feature + "\n\n")

                f.write("## Resources:\n")
                for r in resource_files:
                    f.write(f"- {r}\n")
                f.write("\n")

                f.write("## AI Agent:\n")
                f.write("### User Story\n")
                f.write(result.story.story + "\n\n")

                f.write("### UX Spec\n")
                f.write(result.ux.spec + "\n\n")

                f.write("### Functional Spec\n")
                f.write(result.functional.spec + "\n\n")

                f.write("### Technical Spec\n")
                f.write(result.technical.spec + "\n\n")

                f.write("### Acceptance Criteria\n")
                f.write(result.acceptance.criteria + "\n\n")

                f.write("### Impact Assessment\n")
                f.write(result.impact.summary + "\n")

            visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())
