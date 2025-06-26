"""CheckRacePlanAgent reviews and revises the training plan if needed."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent

from .plan_agent import RacePlan


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "check_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


check_agent = Agent(
    name="CheckRacePlanAgent",
    instructions=_load_prompt(),
    output_type=RacePlan,
)
