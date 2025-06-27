"""Guardrail functions for UserStoryAgent."""

from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)


def _load_prompt(filename: str) -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / filename
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


class GuardrailDecision(BaseModel):
    """Common structure for guardrail agents."""

    flagged: bool
    reason: str


feature_check_agent = Agent(
    name="Feature Input Check",
    instructions=_load_prompt("user_story_input_check.yaml"),
    output_type=GuardrailDecision,
)


@input_guardrail
async def vague_feature_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(feature_check_agent, input, context=ctx.context)
    decision = result.final_output_as(GuardrailDecision)
    return GuardrailFunctionOutput(
        output_info=decision,
        tripwire_triggered=decision.flagged,
    )
