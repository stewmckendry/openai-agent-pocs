from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class UXSpec(BaseModel):
    personas: str
    journey: str


class UXSpecAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_ux.yaml").read_text()
        super().__init__(name="UXSpec", instructions=instructions)

    @tool
    def generate_ux_spec(self, feature: str) -> UXSpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        personas = content
        journey = content
        return UXSpec(personas=personas, journey=journey)

    tools = [generate_ux_spec]
    handoffs: list = []

    def run(self, feature: str) -> UXSpec:
        return self.generate_ux_spec(feature)
