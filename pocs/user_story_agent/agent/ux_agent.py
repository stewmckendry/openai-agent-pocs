"""UX specification agent."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class UXSpec(BaseModel):
    """Structured UX specification."""

    spec: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "ux_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


ux_agent = Agent(
    name="UXAgent",
    instructions=_load_prompt(),
    output_type=UXSpec,
)
