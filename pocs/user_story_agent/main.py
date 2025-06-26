"""Entry point for the User Story Agent PoC.

Requirements:
- Place any feature description text in ``test/sample_input.txt`` to try
the canned example.
- Run with ``python -m pocs.user_story_agent.main`` and enter your own
feature description or pipe the file as stdin.
"""

import asyncio
import sys

from agents import Runner

from .deliverylead import delivery_lead_agent


async def main() -> None:
    feature = input("Enter a feature description: ")
    result = await Runner.run(delivery_lead_agent, feature)
    print("\n--- Technical Specification ---\n")
    print(result.final_output.spec)


if __name__ == "__main__":
    asyncio.run(main())
