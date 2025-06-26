from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.validate_dor import validate_dor


class DoRReview(BaseModel):
    ready: bool


class DoRReviewAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_dor_review.yaml").read_text()
        super().__init__(name="DoRReview", instructions=instructions)

    @tool
    def review(self, story: dict) -> DoRReview:
        ready = validate_dor(story)
        return DoRReview(ready=ready)

    tools = [review]
    handoffs: list = []

    def run(self, story: dict) -> DoRReview:
        return self.review(story)
