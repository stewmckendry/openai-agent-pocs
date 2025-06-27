"""Guardrail functions for TripPlannerAgent."""

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
    output_guardrail,
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


# Helper guardrail agents
input_check_agent = Agent(
    name="Trip Input Check",
    instructions=_load_prompt("guardrail_input_check.yaml"),
    output_type=GuardrailDecision,
)

output_check_agent = Agent(
    name="Trip Output Check",
    instructions=_load_prompt("guardrail_output_check.yaml"),
    output_type=GuardrailDecision,
)


class TripOutput(BaseModel):
    """Wrapper for planner output when validating."""

    response: str


@input_guardrail
async def vague_trip_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_check_agent, input, context=ctx.context)
    decision = result.final_output_as(GuardrailDecision)
    return GuardrailFunctionOutput(
        output_info=decision,
        tripwire_triggered=decision.flagged,
    )


@output_guardrail
async def trip_quality_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    output: TripOutput,
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_check_agent, output.response, context=ctx.context)
    decision = result.final_output_as(GuardrailDecision)
    return GuardrailFunctionOutput(
        output_info=decision,
        tripwire_triggered=decision.flagged,
    )
