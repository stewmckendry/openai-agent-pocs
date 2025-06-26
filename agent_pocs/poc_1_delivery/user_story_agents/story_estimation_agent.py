"""
Purpose: Estimate story size in points for a generated user story
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.estimate_story import story_estimate
import logging

logger = logging.getLogger(__name__)


class StoryEstimate(BaseModel):
    points: int


class StoryEstimationAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[StoryEstimationAgent] start")
        instructions = Path("prompts/user_story_estimate.yaml").read_text()
        super().__init__(
            name="StoryEstimation",
            instructions=instructions,
            model="gpt-4o",
            output_type=StoryEstimate,
            tools=[self.estimate],
            handoffs=[next_agent] if next_agent else [],
        )

    @tool
    def estimate(self, story: str) -> StoryEstimate:
        logger.debug("[StoryEstimationAgent] estimating")
        points = story_estimate({"story": story})
        return StoryEstimate(points=points)

    tools = [estimate]
