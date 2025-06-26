import json
from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class TechContext(BaseModel):
    stack: str
    db: str


class TechContextAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = "Provide tech context to other agents."
        super().__init__(
            name="TechContext",
            instructions=instructions,
            tools=[self.provide_context],
            handoffs=[next_agent] if next_agent else [],
        )
        self.context = json.loads(Path("resources/tech_context.json").read_text())

    @tool
    def provide_context(self) -> TechContext:
        return TechContext(**self.context)

    tools = [provide_context]
