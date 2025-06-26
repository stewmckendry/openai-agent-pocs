from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent
from tools.validate_dor import ValidateDoR


class DoRReview(BaseModel):
    ready: bool


class DoRReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("DoRReview", Path("prompts/user_story_dor_review.yaml"))
        self.validator = ValidateDoR()

    @traceable
    def run(self, story: dict) -> DoRReview:
        ready = self.validator(story)
        output = DoRReview(ready=ready)
        self.record("dor_review", output.model_dump())
        return output
