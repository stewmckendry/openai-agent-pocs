from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent


class FunctionalitySpec(BaseModel):
    functions: str


class FunctionalityAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_functionality.yaml").read_text()
        super().__init__(
            name="Functionality",
            instructions=instructions,
            output_type=FunctionalitySpec,
            handoffs=[next_agent] if next_agent else [],
        )
