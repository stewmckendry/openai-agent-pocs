from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent


class UXSpec(BaseModel):
    personas: str
    journey: str


class UXSpecAgent(BaseAgent):
    def __init__(self):
        super().__init__("UXSpec", Path("prompts/user_story_ux.yaml"))

    @traceable
    def run(self, feature: str) -> UXSpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        personas = content
        journey = content
        output = UXSpec(personas=personas, journey=journey)
        self.record("ux", output.model_dump())
        return output
