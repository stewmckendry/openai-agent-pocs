from pathlib import Path

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent
from .deploy_agent import DeployOutput


class DocsOutput(BaseModel):
    documentation: str


class DocsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Docs", Path("prompts/docs.yaml"))

    @traceable
    def run(self, deploy_output: DeployOutput) -> DocsOutput:
        """Generate documentation for the deployment."""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": deploy_output.model_dump_json()},
            ],
        )
        doc = response.choices[0].message.content
        output = DocsOutput(documentation=doc)
        self.record("docs", output.model_dump())
        return output
