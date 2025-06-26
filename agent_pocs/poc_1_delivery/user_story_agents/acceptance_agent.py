"""
Purpose: Generate Gherkin-style acceptance criteria for a feature
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
import logging

logger = logging.getLogger(__name__)


class AcceptanceCriteria(BaseModel):
    gherkin: str


class AcceptanceCriteriaAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[AcceptanceCriteriaAgent] start")
        instructions = Path("prompts/user_story_acceptance.yaml").read_text()
        super().__init__(
            name="AcceptanceCriteria",
            instructions=instructions,
            model="gpt-4o",
            output_type=AcceptanceCriteria,
            handoffs=[next_agent] if next_agent else [],
        )
