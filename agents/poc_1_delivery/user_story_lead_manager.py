from __future__ import annotations

from openai_agents import Runner
from openai_agents.tracing import Trace

from .user_story_agents.user_story_lead_agent import UserStoryLeadAgent, UserStory


class UserStoryLeadManager:
    """Simple wrapper around ``UserStoryLeadAgent`` to execute a user story run."""

    async def run(self, feature: str) -> tuple[UserStory, Trace]:
        lead_agent = UserStoryLeadAgent()
        result = await Runner.run(lead_agent, {"feature": feature})
        user_story = result.final_output_as(UserStory)
        return user_story, result.trace
