"""Definition of Ready verifier agent."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent


class DoRCheck(BaseModel):
    passes: bool
    story: str
    feedback: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "dor_verifier_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


dor_verifier_agent = Agent(
    name="DoRVerifierAgent",
    instructions=_load_prompt(),
    output_type=DoRCheck,
)
