"""CLI entry point for the Trip Planner Agent PoC.

Requirements:
- Place a travel description in `test/sample_input.txt` to try the example.
- Run with `python -m pocs.trip_planner_agent.main` and enter your own
  trip goals or pipe the file as stdin.
"""

import argparse
import asyncio
import os
from datetime import datetime
from pathlib import Path

from agents import gen_trace_id, trace
from agents.exceptions import (
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
)

from agents.extensions.models.litellm_model import LitellmModel
from .tripmanager import TripPlanningManager, visualize_workflow
from dotenv import load_dotenv


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Model to use (e.g. openai/gpt-4o)")
    parser.add_argument("--api-key", type=str, help="API key for the model")
    args = parser.parse_args()

    load_dotenv()

    model_name = args.model if args.model else os.environ["MODEL"]
    api_key = args.api_key if args.api_key else os.environ["MODEL_API_KEY"]
    model = LitellmModel(model=model_name, api_key=api_key)

    goal = input("Describe your trip goals: ")
    mgr = TripPlanningManager(model=model)
    trace_id = gen_trace_id()
    with trace("trip_planner_poc", trace_id=trace_id):
        try:
            result = await mgr.run(goal, trace_id=trace_id)
        except InputGuardrailTripwireTriggered as exc:
            info = exc.guardrail_result.output.output_info
            print(f"\nInput rejected: {getattr(info, 'reason', '')}")
            return
        except OutputGuardrailTripwireTriggered as exc:
            info = exc.guardrail_result.output.output_info
            print(f"\nInvalid itinerary: {getattr(info, 'reason', '')}")
            return

    print("\n--- Trip Itinerary ---\n")
    print(result.plan.response)

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plan_file = output_dir / f"trip_{timestamp}.md"
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write("# Trip Goals\n")
        f.write(goal + "\n\n")

        f.write("# Research Topics\n")
        for t in result.topics.topics:
            f.write(f"- {t.query} ({t.reason})\n")
        f.write("\n")

        f.write("# Research Summaries\n")
        for r in result.research:
            f.write(r.summary + "\n\n")

        f.write("# Trip Plan\n")
        f.write(result.plan.response)

    visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())
