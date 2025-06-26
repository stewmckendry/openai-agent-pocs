from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class AcceptanceCriteria(BaseModel):
    gherkin: str


class AcceptanceCriteriaAgent(Agent):
    def __init__(self, next_agent: Agent | None = None):
        instructions = Path("prompts/user_story_acceptance.yaml").read_text()
        super().__init__(
            name="AcceptanceCriteria",
            instructions=instructions,
            tools=[self.generate_acceptance],
            handoffs=[next_agent] if next_agent else [],
        )

    @tool
    def generate_acceptance(self, story: str) -> AcceptanceCriteria:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": story},
            ],
        )
        content = resp.choices[0].message.content
        return AcceptanceCriteria(gherkin=content)

    tools = [generate_acceptance]
