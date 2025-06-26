"""
Purpose: Create UX specifications for the requested feature
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent
import logging

logger = logging.getLogger(__name__)


class UXSpec(BaseModel):
    personas: str
    journey: str


class UXSpecAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[UXSpecAgent] start")
        instructions = Path("prompts/user_story_ux.yaml").read_text()
        super().__init__(
            name="UXSpec",
            instructions=instructions,
            model="gpt-4o",
            output_type=UXSpec,
            handoffs=[next_agent] if next_agent else [],
        )
