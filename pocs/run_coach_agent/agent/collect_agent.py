"""CollectRunStatsAgent loads and summarizes recent runs from the CSV file."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent, function_tool


class RunData(BaseModel):
    """Container for the raw CSV of running activities."""

    csv: str


CSV_PATH = Path(__file__).resolve().parent.parent / "resources" / "Activities.csv"


@function_tool(name_override="load_activities", description_override="Load the runner's Activities.csv")
def load_activities() -> str:
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return f.read()


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "collect_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


collect_agent = Agent(
    name="CollectRunStatsAgent",
    instructions=_load_prompt(),
    tools=[load_activities],
    output_type=RunData,
)
