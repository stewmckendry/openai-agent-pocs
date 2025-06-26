from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.validate_dor import validate_dor


class DoRReview(BaseModel):
    ready: bool


class DoRReviewAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_dor_review.yaml").read_text()
        super().__init__(
            name="DoRReview",
            instructions=instructions,
            model="gpt-4o",
            output_type=DoRReview,
            tools=[self.review],
            handoffs=[next_agent] if next_agent else [],
        )

    @tool
    def review(self, story: dict) -> DoRReview:
        ready = validate_dor(story)
        return DoRReview(ready=ready)

    tools = [review]
