from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool
from tools.estimate_story import story_estimate


class StoryEstimate(BaseModel):
    points: int


class StoryEstimationAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_estimate.yaml").read_text()
        super().__init__(
            name="StoryEstimation",
            instructions=instructions,
            model="gpt-4o",
            output_type=StoryEstimate,
            tools=[self.estimate],
            handoffs=[next_agent] if next_agent else [],
        )

    @tool
    def estimate(self, story: str) -> StoryEstimate:
        points = story_estimate({"story": story})
        return StoryEstimate(points=points)

    tools = [estimate]
