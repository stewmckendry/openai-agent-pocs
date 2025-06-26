from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent
from tools.estimate_story import StoryEstimationTool


class StoryEstimate(BaseModel):
    points: int


class StoryEstimationAgent(BaseAgent):
    def __init__(self):
        super().__init__("StoryEstimation", Path("prompts/user_story_estimate.yaml"))
        self.tool = StoryEstimationTool()

    @traceable
    def run(self, story: str) -> StoryEstimate:
        points = self.tool({"story": story})
        output = StoryEstimate(points=points)
        self.record("estimate", output.model_dump())
        return output
