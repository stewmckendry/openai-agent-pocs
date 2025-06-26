from pathlib import Path
from pydantic import BaseModel
from openai_agents.tracing import traceable

from ..base import BaseAgent


class AcceptanceCriteria(BaseModel):
    gherkin: str


class AcceptanceCriteriaAgent(BaseAgent):
    def __init__(self):
        super().__init__("AcceptanceCriteria", Path("prompts/user_story_acceptance.yaml"))

    @traceable
    def run(self, story: str) -> AcceptanceCriteria:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": story},
            ],
        )
        content = resp.choices[0].message.content
        output = AcceptanceCriteria(gherkin=content)
        self.record("acceptance", output.model_dump())
        return output
