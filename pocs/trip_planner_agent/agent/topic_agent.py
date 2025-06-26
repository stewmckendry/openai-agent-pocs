"""TopicAgent generates search topics for trip planning."""

from pathlib import Path
from datetime import datetime
from pydantic import BaseModel
from agents import Agent, function_tool


class ResearchTopic(BaseModel):
    """A topic to research."""

    reason: str
    query: str


class ResearchPlan(BaseModel):
    """Collection of research topics."""

    topics: list[ResearchTopic]


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "topic_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


@function_tool
def get_current_date() -> str:
    """Return today's date in ISO format."""
    return datetime.now().date().isoformat()


topic_agent = Agent(
    name="TopicAgent",
    instructions=_load_prompt(),
    tools=[get_current_date],
    output_type=ResearchPlan,
)
