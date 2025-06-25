from pathlib import Path

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable

from .base import BaseAgent
from .dev_agent import DevOutput
from tools.test_tool import RunUnitTestsTool


class TestOutput(BaseModel):
    success: bool
    details: str


class TestAgent(BaseAgent):
    def __init__(self):
        super().__init__("Test", Path("prompts/test.yaml"))
        self.runner = RunUnitTestsTool()

    @traceable
    def run(self, dev_output: DevOutput) -> TestOutput:
        """Run unit tests and summarize the results."""
        results = self.runner(dev_output.code)
        summary = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": str(results)},
            ],
        ).choices[0].message.content
        output = TestOutput(success=results["success"], details=summary)
        self.record("test", output.model_dump())
        return output
