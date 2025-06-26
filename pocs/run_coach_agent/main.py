"""CLI entry point for the Run Coach Agent PoC.

Requirements:
- Place a Garmin `Activities.csv` file under `resources/` (already provided).
- Run with `python -m pocs.run_coach_agent.main` and enter a race goal when prompted.
"""

import asyncio
from datetime import datetime
from pathlib import Path

from .runcoach import RunCoachManager, visualize_workflow


async def main() -> None:
    goal = input("Describe your race goal: ")
    mgr = RunCoachManager()
    plan = await mgr.run(goal)

    print("\n--- Training Plan ---\n")
    print(plan.plan)

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plan_file = output_dir / f"plan_{timestamp}.md"
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write("# Goal\n")
        f.write(goal + "\n\n")
        f.write(plan.plan)

    visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())

