from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class TechSpec(BaseModel):
    modules: str


class TechSpecAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_tech.yaml").read_text()
        super().__init__(name="TechSpec", instructions=instructions)

    @tool
    def generate_tech_spec(self, feature: str) -> TechSpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        return TechSpec(modules=content)

    tools = [generate_tech_spec]
    handoffs: list = []

    def run(self, feature: str) -> TechSpec:
        return self.generate_tech_spec(feature)
