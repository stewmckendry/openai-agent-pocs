"""
Purpose: Produce a technical specification for the user story
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
import logging

logger = logging.getLogger(__name__)


class TechSpec(BaseModel):
    modules: str


class TechSpecAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[TechSpecAgent] start")
        instructions = Path("prompts/user_story_tech.yaml").read_text()
        super().__init__(
            name="TechSpec",
            instructions=instructions,
            model="gpt-4o",
            output_type=TechSpec,
            handoffs=[next_agent] if next_agent else [],
        )
