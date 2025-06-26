"""
Purpose: Provide project technology context to downstream agents
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

import json
from pathlib import Path
from pydantic import BaseModel
from agents import Agent, function_tool
import logging

logger = logging.getLogger(__name__)


class TechContext(BaseModel):
    stack: str
    db: str


class TechContextAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[TechContextAgent] start")
        instructions = "Provide tech context to other agents."
        super().__init__(
            name="TechContext",
            instructions=instructions,
            model="gpt-4o",
            output_type=TechContext,
            tools=[self.provide_context],
            handoffs=[next_agent] if next_agent else [],
        )
        self.context = json.loads(Path("resources/tech_context.json").read_text())

    @function_tool
    def provide_context(self) -> TechContext:
        logger.debug("[TechContextAgent] provide_context")
        return TechContext(**self.context)

    tools = [provide_context]
