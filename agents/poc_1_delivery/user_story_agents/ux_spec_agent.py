from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent


class UXSpec(BaseModel):
    personas: str
    journey: str


class UXSpecAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_ux.yaml").read_text()
        super().__init__(
            name="UXSpec",
            instructions=instructions,
            model="gpt-4o",
            output_type=UXSpec,
            handoffs=[next_agent] if next_agent else [],
        )
