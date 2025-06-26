"""Technical specification agent.

This module defines ``technical_agent`` which turns a functional
specification into a technical specification. The agent can call the
``architecture`` tool to read the reference architecture from
``resources/tech_architecture.md``.
"""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent, function_tool


class TechnicalSpec(BaseModel):
    """Structured output containing a technical specification."""

    spec: str


ARCH_PATH = Path(__file__).resolve().parent.parent / "resources" / "tech_architecture.md"


@function_tool(name_override="architecture", description_override="Load the reference architecture text")
def load_architecture() -> str:
    """Return the reference architecture document."""
    return ARCH_PATH.read_text(encoding="utf-8")


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "technical_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


technical_agent = Agent(
    name="TechnicalSpecAgent",
    instructions=_load_prompt(),
    tools=[load_architecture],
    output_type=TechnicalSpec,
)
