from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent


class TechSpec(BaseModel):
    modules: str


class TechSpecAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_tech.yaml").read_text()
        super().__init__(
            name="TechSpec",
            instructions=instructions,
            model="gpt-4o",
            output_type=TechSpec,
            handoffs=[next_agent] if next_agent else [],
        )
