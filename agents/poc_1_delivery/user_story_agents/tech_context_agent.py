import json
from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class TechContext(BaseModel):
    stack: str
    db: str


class TechContextAgent(Agent):
    def __init__(self):
        instructions = "Provide tech context to other agents."
        super().__init__(name="TechContext", instructions=instructions)
        self.context = json.loads(Path("resources/tech_context.json").read_text())

    @tool
    def provide_context(self) -> TechContext:
        return TechContext(**self.context)

    tools = [provide_context]
    handoffs: list = []

    def run(self) -> TechContext:
        return self.provide_context()
