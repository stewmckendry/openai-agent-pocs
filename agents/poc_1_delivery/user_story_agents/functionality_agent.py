from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent


class FunctionalitySpec(BaseModel):
    functions: str


class FunctionalityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Functionality", Path("prompts/user_story_functionality.yaml"))

    @traceable
    def run(self, feature: str) -> FunctionalitySpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        output = FunctionalitySpec(functions=content)
        self.record("functionality", output.model_dump())
        return output
