"""
Purpose: Convenience wrapper to run the full user story agent workflow
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from __future__ import annotations

from agents import Runner
from agents.tracing import Trace
import logging

logger = logging.getLogger(__name__)

from .user_story_agents.user_story_lead_agent import UserStoryLeadAgent, UserStory


class UserStoryLeadManager:
    """Simple wrapper around ``UserStoryLeadAgent`` to execute a user story run."""

    async def run(self, feature: str) -> tuple[UserStory, Trace]:
        logger.info("[UserStoryLeadManager] run feature: %s", feature)
        lead_agent = UserStoryLeadAgent()
        result = await Runner.run(lead_agent, {"feature": feature})
        user_story = result.final_output_as(UserStory)
        logger.info("[UserStoryLeadManager] run complete")
        return user_story, result.trace
