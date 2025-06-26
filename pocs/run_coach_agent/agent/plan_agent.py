"""PlanRaceAgent creates a week-by-week training schedule."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class RacePlan(BaseModel):
    """Textual training plan."""

    plan: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "plan_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


plan_agent = Agent(
    name="PlanRaceAgent",
    instructions=_load_prompt(),
    output_type=RacePlan,
)
