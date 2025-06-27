"""CLI entry point for the Run Coach Agent PoC.

Requirements:
- Place a Garmin `Activities.csv` file under `resources/` (already provided).
- Run with `python -m pocs.run_coach_agent.main` and enter a race goal when prompted.
"""

import argparse
import asyncio
import os
from datetime import datetime
from pathlib import Path

from agents import gen_trace_id, trace
from agents.exceptions import InputGuardrailTripwireTriggered
from agents.extensions.models.litellm_model import LitellmModel
from .runcoach import RunCoachManager, visualize_workflow


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Model to use (e.g. openai/gpt-4o)")
    parser.add_argument("--api-key", type=str, help="API key for the model")
    args = parser.parse_args()

    model_name = args.model if args.model else os.environ["MODEL"]
    api_key = args.api_key if args.api_key else os.environ["MODEL_API_KEY"]
    model = LitellmModel(model=model_name, api_key=api_key)

    goal = input("Describe your race goal: ")
    mgr = RunCoachManager(model=model)
    trace_id = gen_trace_id()
    with trace("run_coach_poc", trace_id=trace_id):
        try:
            result = await mgr.run(goal, trace_id=trace_id)
        except InputGuardrailTripwireTriggered as exc:
            info = exc.guardrail_result.output.output_info
            print(f"\nInput rejected: {getattr(info, 'reason', '')}")
            return

    print("\n--- Training Plan ---\n")
    print(result.plan.plan)

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plan_file = output_dir / f"plan_{timestamp}.md"
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write("# Your Race Input\n")
        f.write(goal + "\n\n")

        f.write("# Race Goal\n")
        f.write(str(result.goal) + "\n\n")

        f.write("# Current Run Stats\n")
        f.write(result.runs.csv + "\n\n")

        f.write("# Run Analysis\n")
        f.write(result.analysis.analysis + "\n\n")

        f.write("# Training Plan\n")
        f.write(result.plan.plan)

    visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())

