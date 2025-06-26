from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.impact_assess import impact_assessment


class ImpactAssessment(BaseModel):
    impact: str


class ImpactAssessmentAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_impact.yaml").read_text()
        super().__init__(name="ImpactAssessment", instructions=instructions)

    @tool
    def assess(self, story: dict) -> ImpactAssessment:
        impact = impact_assessment(story)
        return ImpactAssessment(impact=impact)

    tools = [assess]
    handoffs: list = []

    def run(self, story: dict) -> ImpactAssessment:
        return self.assess(story)
