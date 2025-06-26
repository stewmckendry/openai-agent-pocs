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
    story = await mgr.run(feature)
    print("\n--- User Story ---\n")
    print(story.story)

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    story_file = output_dir / f"story_{timestamp}.md"
    with open(story_file, "w", encoding="utf-8") as f:
        f.write("# Feature Input\n")
        f.write(feature + "\n\n")
        f.write(story.story)

    visualize_workflow(filename=str(output_dir / f"workflow_{timestamp}.png"))


if __name__ == "__main__":
    asyncio.run(main())
