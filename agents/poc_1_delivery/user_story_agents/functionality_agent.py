"""
Purpose: Outline core functionality for the proposed feature
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
import logging

logger = logging.getLogger(__name__)


class FunctionalitySpec(BaseModel):
    functions: str


class FunctionalityAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[FunctionalityAgent] start")
        instructions = Path("prompts/user_story_functionality.yaml").read_text()
        super().__init__(
            name="Functionality",
            instructions=instructions,
            model="gpt-4o",
            output_type=FunctionalitySpec,
            handoffs=[next_agent] if next_agent else [],
        )
