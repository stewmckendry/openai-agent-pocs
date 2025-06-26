from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent


class TechSpec(BaseModel):
    modules: str


class TechSpecAgent(BaseAgent):
    def __init__(self):
        super().__init__("TechSpec", Path("prompts/user_story_tech.yaml"))

    @traceable
    def run(self, feature: str) -> TechSpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        output = TechSpec(modules=content)
        self.record("tech", output.model_dump())
        return output
