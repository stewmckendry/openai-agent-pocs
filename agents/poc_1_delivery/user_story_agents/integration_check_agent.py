"""
Purpose: Verify integration considerations for the feature
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
import logging

logger = logging.getLogger(__name__)


class IntegrationCheck(BaseModel):
    notes: str


class IntegrationCheckAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[IntegrationCheckAgent] start")
        instructions = Path("prompts/user_story_impact.yaml").read_text()
        super().__init__(
            name="IntegrationCheck",
            instructions=instructions,
            model="gpt-4o",
            output_type=IntegrationCheck,
            handoffs=[next_agent] if next_agent else [],
        )
