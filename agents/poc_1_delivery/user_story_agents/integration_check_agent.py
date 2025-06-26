from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent


class IntegrationCheck(BaseModel):
    notes: str


class IntegrationCheckAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_impact.yaml").read_text()
        super().__init__(
            name="IntegrationCheck",
            instructions=instructions,
            output_type=IntegrationCheck,
            handoffs=[next_agent] if next_agent else [],
        )
