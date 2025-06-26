from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent


class AcceptanceCriteria(BaseModel):
    gherkin: str


class AcceptanceCriteriaAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_acceptance.yaml").read_text()
        super().__init__(
            name="AcceptanceCriteria",
            instructions=instructions,
            model="gpt-4o",
            output_type=AcceptanceCriteria,
            handoffs=[next_agent] if next_agent else [],
        )
