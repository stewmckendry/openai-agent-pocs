"""Entry point for the User Story Agent PoC.

Requirements:
- Place any feature description text in ``test/sample_input.txt`` to try
  the canned example.
- Run with ``python -m pocs.user_story_agent.main`` and enter your own
  feature description or pipe the file as stdin.
"""

import asyncio
from pathlib import Path
from datetime import datetime

from .deliverylead import DeliveryLeadManager, visualize_workflow


async def main() -> None:
    feature = input("Enter a feature description: ")
    mgr = DeliveryLeadManager()
    result = await mgr.run(feature)
    print("\n--- User Story ---\n")
    print(result.story.story)

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    story_file = output_dir / f"story_{timestamp}.md"
    with open(story_file, "w", encoding="utf-8") as f:
        f.write("# Feature Input\n")
        f.write(feature + "\n\n")

        f.write("# User Story\n")
        f.write(result.story.story + "\n\n")

        f.write("# UX Spec\n")
        f.write(result.ux.spec + "\n\n")

        f.write("# Functional Spec\n")
        f.write(result.functional.spec + "\n\n")

        f.write("# Technical Spec\n")
        f.write(result.technical.spec + "\n\n")

        f.write("# Acceptance Criteria\n")
        f.write(result.acceptance.criteria + "\n\n")

        f.write("# Impact Assessment\n")
        f.write(result.impact.summary + "\n")

    visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())
