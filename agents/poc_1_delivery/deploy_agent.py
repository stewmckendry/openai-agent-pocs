from pathlib import Path

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent
from .test_agent import TestOutput


class DeployOutput(BaseModel):
    version: str
    notes: str


class DeployAgent(BaseAgent):
    def __init__(self):
        super().__init__("Deploy", Path("prompts/deploy.yaml"))

    @traceable
    def run(self, test_output: TestOutput) -> DeployOutput:
        """Create a deployment plan based on test results."""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": test_output.model_dump_json()},
            ],
        )
        plan = response.choices[0].message.content.split("\n")
        output = DeployOutput(version=plan[0], notes="\n".join(plan[1:]))
        self.record("deploy", output.model_dump())
        return output
