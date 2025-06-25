from pathlib import Path
from typing import List

from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent
from .po_planner_agent import Story, PlanningOutput
from tools.validate_dor import ValidateDoR


class RefinedStories(BaseModel):
    stories: List[Story]


class DoRRefinerAgent(BaseAgent):
    def __init__(self):
        super().__init__("DoRRefiner", Path("prompts/dor_refiner.yaml"))
        self.validator = ValidateDoR()

    @traceable
    def run(self, stories: PlanningOutput) -> RefinedStories:
        refined = []
        for s in stories.stories:
            ready = self.validator(s.model_dump())
            refined.append(s.model_copy(update={"ready": ready}))
        output = RefinedStories(stories=refined)
        self.record("refine", output.model_dump())
        return output
