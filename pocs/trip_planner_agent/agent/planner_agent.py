"""PlannerAgent synthesizes research into a trip itinerary."""
from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class TripPlan(BaseModel):
    """Final travel plan."""

    summary: str
    itinerary: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "plan_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


planner_agent = Agent(
    name="PlannerAgent",
    instructions=_load_prompt(),
    output_type=TripPlan,
)
