import json
from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tracing import Trace, traceable


class TechContext(BaseModel):
    stack: str
    db: str


class TechContextAgent(Agent):
    def __init__(self):
        instructions = "Provide tech context to other agents."
        super().__init__(name="TechContext", instructions=instructions)
        self.trace = Trace("TechContext")
        self.context = json.loads(Path("resources/tech_context.json").read_text())

    def record(self, step: str, output: dict):
        self.trace.add_event(step, output)

    @traceable
    def run(self) -> TechContext:
        output = TechContext(**self.context)
        self.record("context", output.model_dump())
        return output
