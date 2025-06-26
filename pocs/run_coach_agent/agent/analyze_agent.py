"""AnalyzeRunStatsAgent finds patterns and gaps in the user's running history."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class StatsAnalysis(BaseModel):
    """Narrative assessment of the runner's current state."""

    analysis: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "analyze_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


analyze_agent = Agent(
    name="AnalyzeRunStatsAgent",
    instructions=_load_prompt(),
    output_type=StatsAnalysis,
)
