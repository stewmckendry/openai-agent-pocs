"""Entry point for the User Story Agent PoC.

Requirements:
- Place any feature description text in ``test/sample_input.txt`` to try
  the canned example.
- Run with ``python -m pocs.user_story_agent.main`` and enter your own
  feature description or pipe the file as stdin.
"""

import asyncio

from .deliverylead import DeliveryLeadManager, visualize_workflow


async def main() -> None:
    feature = input("Enter a feature description: ")
    mgr = DeliveryLeadManager()
    story = await mgr.run(feature)
    print("\n--- User Story ---\n")
    print(story.story)
    visualize_workflow()


if __name__ == "__main__":
    asyncio.run(main())
