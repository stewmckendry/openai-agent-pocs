"""
Purpose: Validate that a user story meets the Definition of Ready
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent, function_tool
from tools.validate_dor import validate_dor
import logging

logger = logging.getLogger(__name__)


class DoRReview(BaseModel):
    ready: bool


class DoRReviewAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[DoRReviewAgent] start")
        instructions = Path("prompts/user_story_dor_review.yaml").read_text()
        super().__init__(
            name="DoRReview",
            instructions=instructions,
            model="gpt-4o",
            output_type=DoRReview,
            tools=[self.review],
            handoffs=[next_agent] if next_agent else [],
        )

    @function_tool
    def review(self, story: dict) -> DoRReview:
        logger.debug("[DoRReviewAgent] review")
        ready = validate_dor(story)
        return DoRReview(ready=ready)

    tools = [review]
