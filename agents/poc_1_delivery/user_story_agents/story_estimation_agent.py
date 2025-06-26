from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.estimate_story import story_estimate


class StoryEstimate(BaseModel):
    points: int


class StoryEstimationAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_estimate.yaml").read_text()
        super().__init__(name="StoryEstimation", instructions=instructions)

    @tool
    def estimate(self, story: str) -> StoryEstimate:
        points = story_estimate({"story": story})
        return StoryEstimate(points=points)

    tools = [estimate]
    handoffs: list = []

    def run(self, story: str) -> StoryEstimate:
        return self.estimate(story)
