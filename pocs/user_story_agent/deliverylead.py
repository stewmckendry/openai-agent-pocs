"""Delivery Lead agent and helpers.

This module orchestrates the user story workflow by delegating to
specialized sub-agents in sequence. The pipeline generates UX,
functional, technical, acceptance, impact, and estimation results before
drafting the final user story and verifying it against the Definition of
Ready (DoR). All intermediate results are returned in a structured
``UserStoryPipelineOutput`` model.
"""

from __future__ import annotations

from rich.console import Console
from pydantic import BaseModel

from agents import Agent, Runner, gen_trace_id, trace
from agents.extensions.visualization import draw_graph

from .agent.functional_agent import FunctionalSpec, functional_agent
from .agent.technical_agent import TechnicalSpec, technical_agent
from .agent.ux_agent import UXSpec, ux_agent
from .agent.acceptance_agent import AcceptanceCriteria, acceptance_agent
from agents.mcp import MCPServer
from .agent.impact_agent import ImpactSummary, build_impact_agent
from .agent.estimate_agent import StoryPointEstimate, estimate_agent
from .agent.dor_verifier_agent import DoRCheck, dor_verifier_agent
from .agent.user_story_writer import UserStory, user_story_writer_agent
from .printer import Printer


DELIVERY_PROMPT = (
    "You are a software delivery lead. Given a feature description you "
    "delegate to UX, functional, technical, acceptance, impact, estimation, "
    "story writing and DoR verification agents to produce a ready user story."
)


# Agent object used only for workflow visualization
_impact_placeholder = Agent(
    name="ImpactAssessmentAgent",
    instructions="Placeholder",
)

delivery_lead_agent = Agent(
    name="DeliveryLeadAgent",
    instructions=DELIVERY_PROMPT,
    handoffs=[
        ux_agent,
        functional_agent,
        technical_agent,
        acceptance_agent,
        _impact_placeholder,
        estimate_agent,
        user_story_writer_agent,
        dor_verifier_agent,
    ],
    output_type=UserStory,
)


class UserStoryPipelineOutput(BaseModel):
    """Aggregate results from the delivery lead workflow."""

    ux: UXSpec
    functional: FunctionalSpec
    technical: TechnicalSpec
    acceptance: AcceptanceCriteria
    impact: ImpactSummary
    estimate: StoryPointEstimate
    story: UserStory
    dor: DoRCheck


class DeliveryLeadManager:
    """Orchestrates the sequential user story generation workflow."""

    def __init__(self, mcp_server: MCPServer, max_dor_iterations: int = 5) -> None:
        self.console = Console()
        self.printer = Printer(self.console)
        self.max_dor_iterations = max_dor_iterations
        self.mcp_server = mcp_server

    async def run(self, feature: str) -> UserStoryPipelineOutput:
        trace_id = gen_trace_id()
        with trace("user_story_pipeline", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}",
                is_done=True,
                hide_checkmark=True,
            )
            print(f"https://platform.openai.com/traces/trace?trace_id={trace_id}")

            with trace("ux_spec"):
                self.printer.update_item("ux", "Generating UX spec...")
                ux_result = await Runner.run(ux_agent, feature)
                ux = ux_result.final_output_as(UXSpec)
                self.printer.update_item("ux", ux.spec, is_done=True)

            with trace("functional_spec"):
                self.printer.update_item("functional", "Generating functional spec...")
                func_input = f"Feature: {feature}\nUX spec:\n{ux.spec}"
                func_result = await Runner.run(functional_agent, func_input)
                functional = func_result.final_output_as(FunctionalSpec)
                self.printer.update_item("functional", functional.spec, is_done=True)

            with trace("technical_spec"):
                self.printer.update_item("technical", "Generating technical spec...")
                tech_result = await Runner.run(technical_agent, functional.spec)
                technical = tech_result.final_output_as(TechnicalSpec)
                self.printer.update_item("technical", technical.spec, is_done=True)

            with trace("acceptance_criteria"):
                self.printer.update_item("acceptance", "Writing acceptance criteria...")
                acc_input = (
                    f"Functional specification:\n{functional.spec}\n\n"
                    f"Technical specification:\n{technical.spec}"
                )
                acc_result = await Runner.run(acceptance_agent, acc_input)
                acceptance = acc_result.final_output_as(AcceptanceCriteria)
                self.printer.update_item("acceptance", acceptance.criteria, is_done=True)

            with trace("impact_assessment"):
                self.printer.update_item("impact", "Assessing impact...")
                impact_input = (
                    f"Functional specification:\n{functional.spec}\n\n"
                    f"Technical specification:\n{technical.spec}"
                )
                impact_agent = build_impact_agent(self.mcp_server)
                impact_result = await Runner.run(impact_agent, impact_input)
                impact = impact_result.final_output_as(ImpactSummary)
                self.printer.update_item("impact", impact.summary, is_done=True)

            with trace("storypoint_estimate"):
                self.printer.update_item("estimate", "Estimating story points...")
                est_result = await Runner.run(estimate_agent, impact.summary)
                estimate = est_result.final_output_as(StoryPointEstimate)
                self.printer.update_item("estimate", str(estimate.points), is_done=True)

            with trace("user_story"):
                self.printer.update_item("story", "Writing user story...")
                story_input = (
                    f"UX spec:\n{ux.spec}\n\n"
                    f"Functional spec:\n{functional.spec}\n\n"
                    f"Technical spec:\n{technical.spec}\n\n"
                    f"Acceptance criteria:\n{acceptance.criteria}\n\n"
                    f"Impact:\n{impact.summary}\n\n"
                    f"Story points: {estimate.points}"
                )
                story_result = await Runner.run(user_story_writer_agent, story_input)
                story = story_result.final_output_as(UserStory)
                self.printer.update_item("story", "Story drafted", is_done=True)

            passes = False
            iterations = 0
            feedback = ""
            while not passes and iterations < self.max_dor_iterations:
                with trace("dor_verification"):
                    self.printer.update_item("dor", "Checking DoR...")
                    dor_input = story.story
                    if feedback:
                        dor_input += f"\n\nPrevious feedback:\n{feedback}"
                    dor_result = await Runner.run(dor_verifier_agent, dor_input)
                    dor = dor_result.final_output_as(DoRCheck)
                    passes = dor.passes
                    story.story = dor.story
                    feedback = dor.feedback
                    iterations += 1
                    if not passes and iterations < self.max_dor_iterations:
                        self.printer.update_item(
                            "dor", f"Story failed DoR: {dor.feedback} Rewriting..."
                        )
                    elif not passes:
                        self.printer.update_item(
                            "dor", "Max DoR iterations reached", is_done=True
                        )
                    else:
                        self.printer.update_item("dor", "DoR passed", is_done=True)

            self.printer.end()
            return UserStoryPipelineOutput(
                ux=ux,
                functional=functional,
                technical=technical,
                acceptance=acceptance,
                impact=impact,
                estimate=estimate,
                story=story,
                dor=dor,
            )


def visualize_workflow(filename: str | None = None):
    """Generate a graphviz visualization of the agent workflow."""

    return draw_graph(delivery_lead_agent, filename=filename)
