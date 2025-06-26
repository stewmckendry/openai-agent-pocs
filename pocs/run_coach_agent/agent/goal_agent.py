"""GoalRaceAgent converts a free form race description into structured data."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class RaceGoal(BaseModel):
    """Structured race goal information."""

    race_type: str
    race_date: str
    distance_km: float
    time_goal: str
    weeks_to_train: int


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "goal_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


goal_agent = Agent(
    name="GoalRaceAgent",
    instructions=_load_prompt(),
    output_type=RaceGoal,
)
