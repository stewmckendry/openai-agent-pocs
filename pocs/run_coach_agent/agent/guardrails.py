"""Guardrail functions for RunCoachAgent."""

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
    path = Path(__file__).resolve().parents[3] / "prompts" / "guardrails" / filename
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


class GuardrailDecision(BaseModel):
    """Common structure for guardrail agents."""

    flagged: bool
    reason: str


goal_check_agent = Agent(
    name="Race Goal Input Check",
    instructions=_load_prompt("goal_input_check.yaml"),
    output_type=GuardrailDecision,
)


@input_guardrail
async def race_goal_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(goal_check_agent, input, context=ctx.context)
    decision = result.final_output_as(GuardrailDecision)
    return GuardrailFunctionOutput(
        output_info=decision,
        tripwire_triggered=decision.flagged,
    )
