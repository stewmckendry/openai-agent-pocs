from pathlib import Path

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent


class EvaluationOutput(BaseModel):
    needs_changes: bool


class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Evaluator", Path("prompts/evaluator.yaml"))

    @traceable
    def run(self, stage_output: BaseModel) -> EvaluationOutput:
        """Evaluate an intermediate stage and flag if changes are needed."""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": stage_output.model_dump_json()},
            ],
        )
        content = response.choices[0].message.content.lower()
        output = EvaluationOutput(needs_changes="change" in content)
        self.record("evaluate", output.model_dump())
        return output
