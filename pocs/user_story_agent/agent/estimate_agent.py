"""Story point estimation agent."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class StoryPointEstimate(BaseModel):
    points: int


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "estimation_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


estimate_agent = Agent(
    name="StorypointEstimatorAgent",
    instructions=_load_prompt(),
    output_type=StoryPointEstimate,
)
