from pathlib import Path
from pydantic import BaseModel
from openai_agents import Agent
from openai_agents.tools import tool


class FunctionalitySpec(BaseModel):
    functions: str


class FunctionalityAgent(Agent):
    def __init__(self):
        instructions = Path("prompts/user_story_functionality.yaml").read_text()
        super().__init__(name="Functionality", instructions=instructions)

    @tool
    def generate_functionality(self, feature: str) -> FunctionalitySpec:
        import openai

        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": feature},
            ],
        )
        content = resp.choices[0].message.content
        return FunctionalitySpec(functions=content)

    tools = [generate_functionality]
    handoffs: list = []

    def run(self, feature: str) -> FunctionalitySpec:
        return self.generate_functionality(feature)
