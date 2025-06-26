from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent


class IntegrationCheck(BaseModel):
    notes: str


class IntegrationCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntegrationCheck", Path("prompts/user_story_impact.yaml"))

    @traceable
    def run(self, feature: str) -> IntegrationCheck:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        output = IntegrationCheck(notes=resp.choices[0].message.content)
        self.record("integration", output.model_dump())
        return output
