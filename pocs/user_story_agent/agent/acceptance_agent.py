"""Acceptance criteria agent."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class AcceptanceCriteria(BaseModel):
    criteria: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "acceptance_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


acceptance_agent = Agent(
    name="AcceptanceCriteriaAgent",
    instructions=_load_prompt(),
    output_type=AcceptanceCriteria,
)
