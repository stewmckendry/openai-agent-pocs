from __future__ import annotations

from pydantic import BaseModel

from openai_agents import Runner, gen_trace_id, trace

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
        trace_id = gen_trace_id()
        with trace("User story trace", trace_id=trace_id):
            context_res = await Runner.run(self.context_agent, feature)
            context = context_res.final_output_as(TechContext)

            ux_res = await Runner.run(self.ux_agent, feature)
            ux = ux_res.final_output_as(UXSpec)

            func_res = await Runner.run(self.func_agent, feature)
            functionality = func_res.final_output_as(FunctionalitySpec)

            tech_res = await Runner.run(self.tech_agent, feature)
            tech = tech_res.final_output_as(TechSpec)

            acc_res = await Runner.run(self.acceptance_agent, feature)
            acceptance = acc_res.final_output_as(AcceptanceCriteria)

            est_res = await Runner.run(self.estimation_agent, feature)
            estimate = est_res.final_output_as(StoryEstimate)

            dor_res = await Runner.run(self.dor_agent, feature)
            dor = dor_res.final_output_as(DoRReview)

            impact_res = await Runner.run(self.impact_agent, feature)
            impact = impact_res.final_output_as(ImpactAssessment)

            int_res = await Runner.run(self.integration_agent, feature)
            integration = int_res.final_output_as(IntegrationCheck)

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
