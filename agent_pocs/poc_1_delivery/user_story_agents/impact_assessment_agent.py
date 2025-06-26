"""
Purpose: Assess impact of implementing the feature on existing systems
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent
from agents.tools import tool
from tools.impact_assess import impact_assessment
import logging

logger = logging.getLogger(__name__)


class ImpactAssessment(BaseModel):
    impact: str


class ImpactAssessmentAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        logger.info("[ImpactAssessmentAgent] start")
        instructions = Path("prompts/user_story_impact.yaml").read_text()
        super().__init__(
            name="ImpactAssessment",
            instructions=instructions,
            model="gpt-4o",
            output_type=ImpactAssessment,
            tools=[self.assess],
            handoffs=[next_agent] if next_agent else [],
        )

    @tool
    def assess(self, story: dict) -> ImpactAssessment:
        logger.debug("[ImpactAssessmentAgent] assess")
        impact = impact_assessment(story)
        return ImpactAssessment(impact=impact)

    tools = [assess]
