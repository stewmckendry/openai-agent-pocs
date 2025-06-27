"""CLI entry point for the Trip Planner Agent PoC.

Requirements:
- Place a travel description in `test/sample_input.txt` to try the example.
- Run with `python -m pocs.trip_planner_agent.main` and enter your own
  trip goals or pipe the file as stdin.
"""

import asyncio
from datetime import datetime
from pathlib import Path

from agents.exceptions import (
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
)

from .tripmanager import TripPlanningManager, visualize_workflow


async def main() -> None:
    goal = input("Describe your trip goals: ")
    mgr = TripPlanningManager()
    try:
        result = await mgr.run(goal)
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
