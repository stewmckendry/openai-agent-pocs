from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class IntegrationCheck(BaseModel):
    notes: str


class IntegrationCheckAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_impact.yaml").read_text()
        super().__init__(name="IntegrationCheck", instructions=instructions)

    @tool
    def check_integration(self, feature: str) -> IntegrationCheck:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        return IntegrationCheck(notes=resp.choices[0].message.content)

    tools = [check_integration]
    handoffs: list = []

    def run(self, feature: str) -> IntegrationCheck:
        return self.check_integration(feature)
