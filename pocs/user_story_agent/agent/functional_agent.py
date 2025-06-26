"""Functional specification agent.

This module defines ``functional_agent`` which transforms a feature
request into a short functional specification. The prompt text is loaded
from ``prompts/functional_prompt.yaml``. The agent returns a
``FunctionalSpec`` model with the spec string.
"""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class FunctionalSpec(BaseModel):
    """Structured output containing a functional specification."""

    spec: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "functional_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Skip the first line ("prompt: |\n") and return the rest
    return "".join(lines[1:]).lstrip()


functional_agent = Agent(
    name="FunctionalSpecAgent",
    instructions=_load_prompt(),
    output_type=FunctionalSpec,
)
