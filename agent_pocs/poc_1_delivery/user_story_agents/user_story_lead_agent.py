"""
Purpose: Orchestrate all agents to generate a complete user story
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from __future__ import annotations

from pydantic import BaseModel

from agents import Runner, custom_span, gen_trace_id, trace
from rich.console import Console

from .printer import Printer
import logging

logger = logging.getLogger(__name__)

from .tech_context_agent import TechContextAgent, TechContext
from .ux_spec_agent import UXSpecAgent, UXSpec
from .functionality_agent import FunctionalityAgent, FunctionalitySpec
from .tech_spec_agent import TechSpecAgent, TechSpec
from .acceptance_agent import AcceptanceCriteriaAgent, AcceptanceCriteria
from .story_estimation_agent import StoryEstimationAgent, StoryEstimate
from .dor_review_agent import DoRReviewAgent, DoRReview
from .impact_assessment_agent import ImpactAssessmentAgent, ImpactAssessment
from .integration_check_agent import IntegrationCheckAgent, IntegrationCheck


class UserStory(BaseModel):
    """Aggregated user story output."""

    tech_context: TechContext
    ux_spec: UXSpec
    functionality: FunctionalitySpec
    tech_spec: TechSpec
    acceptance: AcceptanceCriteria
    estimate: StoryEstimate
    dor_review: DoRReview
    impact_assessment: ImpactAssessment
    integration_check: IntegrationCheck


class UserStoryLeadAgent:
    """Manager that orchestrates the user story generation flow."""

    def __init__(self) -> None:
        logger.info("[UserStoryLeadAgent] start")
        self.console = Console()
        self.printer = Printer(self.console)
        self.context_agent = TechContextAgent()
        self.ux_agent = UXSpecAgent()
        self.func_agent = FunctionalityAgent()
        self.tech_agent = TechSpecAgent()
        self.acceptance_agent = AcceptanceCriteriaAgent()
        self.estimation_agent = StoryEstimationAgent()
        self.dor_agent = DoRReviewAgent()
        self.impact_agent = ImpactAssessmentAgent()
        self.integration_agent = IntegrationCheckAgent()

    async def run(self, feature: str) -> UserStory:
        """Run the full user story workflow for the provided feature."""
        logger.info("[UserStoryLeadAgent] run feature: %s", feature)
        trace_id = gen_trace_id()
        with trace("User story trace", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}",
                is_done=True,
                hide_checkmark=True,
            )

            self.printer.update_item("context", "Generating tech context...")
            with custom_span("Tech context"):
                context_res = await Runner.run(self.context_agent, feature)
            self.printer.mark_item_done("context")
            context = context_res.final_output_as(TechContext)

            self.printer.update_item("ux", "Creating UX spec...")
            with custom_span("UX spec"):
                ux_res = await Runner.run(self.ux_agent, feature)
            self.printer.mark_item_done("ux")
            ux = ux_res.final_output_as(UXSpec)

            self.printer.update_item("functionality", "Outlining functionality...")
            with custom_span("Functionality"):
                func_res = await Runner.run(self.func_agent, feature)
            self.printer.mark_item_done("functionality")
            functionality = func_res.final_output_as(FunctionalitySpec)

            self.printer.update_item("tech_spec", "Drafting tech spec...")
            with custom_span("Tech spec"):
                tech_res = await Runner.run(self.tech_agent, feature)
            self.printer.mark_item_done("tech_spec")
            tech = tech_res.final_output_as(TechSpec)

            self.printer.update_item("acceptance", "Writing acceptance criteria...")
            with custom_span("Acceptance criteria"):
                acc_res = await Runner.run(self.acceptance_agent, feature)
            self.printer.mark_item_done("acceptance")
            acceptance = acc_res.final_output_as(AcceptanceCriteria)

            self.printer.update_item("estimate", "Estimating story size...")
            with custom_span("Estimate"):
                est_res = await Runner.run(self.estimation_agent, feature)
            self.printer.mark_item_done("estimate")
            estimate = est_res.final_output_as(StoryEstimate)

            self.printer.update_item("dor_review", "Running DoR review...")
            with custom_span("DoR review"):
                dor_res = await Runner.run(self.dor_agent, feature)
            self.printer.mark_item_done("dor_review")
            dor = dor_res.final_output_as(DoRReview)

            self.printer.update_item("impact", "Assessing impact...")
            with custom_span("Impact assessment"):
                impact_res = await Runner.run(self.impact_agent, feature)
            self.printer.mark_item_done("impact")
            impact = impact_res.final_output_as(ImpactAssessment)

            self.printer.update_item("integration", "Checking integration...")
            with custom_span("Integration check"):
                int_res = await Runner.run(self.integration_agent, feature)
            self.printer.mark_item_done("integration")
            integration = int_res.final_output_as(IntegrationCheck)

            self.printer.end()
            logger.info("[UserStoryLeadAgent] workflow complete")

        return UserStory(
            tech_context=context,
            ux_spec=ux,
            functionality=functionality,
            tech_spec=tech,
            acceptance=acceptance,
            estimate=estimate,
            dor_review=dor,
            impact_assessment=impact,
            integration_check=integration,
        )
