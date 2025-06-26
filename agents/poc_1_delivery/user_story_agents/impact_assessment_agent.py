from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent
from tools.impact_assess import ImpactAssessmentTool


class ImpactAssessment(BaseModel):
    impact: str


class ImpactAssessmentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ImpactAssessment", Path("prompts/user_story_impact.yaml"))
        self.tool = ImpactAssessmentTool()

    @traceable
    def run(self, story: dict) -> ImpactAssessment:
        impact = self.tool(story)
        output = ImpactAssessment(impact=impact)
        self.record("impact", output.model_dump())
        return output
