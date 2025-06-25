from pathlib import Path
from typing import Dict, List

import openai
from pydantic import BaseModel

from .base import BaseAgent
from openai_agents.tracing import traceable


class Story(BaseModel):
    id: str
    title: str
    description: str
    ready: bool = False


class PlanningOutput(BaseModel):
    stories: List[Story]


class POPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("POPlanner", Path("prompts/po_planner.yaml"))

    @traceable
    def run(self, feature_idea: str) -> PlanningOutput:
        """Generate user stories for the feature idea using an LLM call."""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": self.instructions}, {"role": "user", "content": feature_idea}],
        )
        ideas = response.choices[0].message.content.split("\n")
        stories = [
            Story(id=f"STORY-{i+1}", title=line.strip(), description=line.strip())
            for i, line in enumerate(ideas[:3])
            if line.strip()
        ]
        output = PlanningOutput(stories=stories)
        self.record("plan", output.model_dump())
        return output
