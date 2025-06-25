from pathlib import Path

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent
from .dor_refiner_agent import RefinedStories


class DevOutput(BaseModel):
    code: str


class DevAgent(BaseAgent):
    def __init__(self):
        super().__init__("Dev", Path("prompts/dev.yaml"))

    @traceable
    def run(self, stories: RefinedStories) -> DevOutput:
        """Generate prototype code for the refined stories."""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": stories.model_dump_json()},
            ],
        )
        code = response.choices[0].message.content
        output = DevOutput(code=code)
        self.record("develop", output.model_dump())
        return output
