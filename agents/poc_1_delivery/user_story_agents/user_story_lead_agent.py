from typing import Dict

from openai_agents import Agent
from openai_agents.tools import tool

from .ux_spec_agent import UXSpecAgent, UXSpec
from .functionality_agent import FunctionalityAgent, FunctionalitySpec
from .tech_spec_agent import TechSpecAgent, TechSpec
from .acceptance_agent import AcceptanceCriteriaAgent, AcceptanceCriteria
from .story_estimation_agent import StoryEstimationAgent, StoryEstimate
from .dor_review_agent import DoRReviewAgent, DoRReview
from .impact_assessment_agent import ImpactAssessmentAgent, ImpactAssessment
from .tech_context_agent import TechContextAgent, TechContext
from .integration_check_agent import IntegrationCheckAgent, IntegrationCheck


class UserStoryLeadAgent(Agent):
    """Generate Definition of Ready user stories from a feature description."""

    def __init__(self):
        instructions = "Generate Definition of Ready user stories from a feature description."
        super().__init__(name="UserStoryLead", instructions=instructions)
        self.ux = UXSpecAgent()
        self.func = FunctionalityAgent()
        self.tech = TechSpecAgent()
        self.acceptance = AcceptanceCriteriaAgent()
        self.estimate = StoryEstimationAgent()
        self.dor = DoRReviewAgent()
        self.impact = ImpactAssessmentAgent()
        self.context = TechContextAgent()
        self.integration = IntegrationCheckAgent()

    @tool
    def generate(self, feature: str) -> Dict:
        output: Dict[str, Dict] = {}

        context: TechContext = self.context.run()
        output["tech_context"] = context.model_dump()

        ux: UXSpec = self.ux.run(feature)
        output["ux"] = ux.model_dump()

        functionality: FunctionalitySpec = self.func.run(feature)
        output["functionality"] = functionality.model_dump()

        tech: TechSpec = self.tech.run(feature)
        output["tech_spec"] = tech.model_dump()

        acceptance: AcceptanceCriteria = self.acceptance.run(feature)
        output["acceptance"] = acceptance.model_dump()

        estimate: StoryEstimate = self.estimate.run(feature)
        output["estimate"] = estimate.model_dump()

        dor: DoRReview = self.dor.run(
            {
                "id": "STORY-1",
                "summary": feature,
                "description": functionality.functions,
                "acceptance_criteria": [acceptance.gherkin],
                "estimate": estimate.points,
            }
        )
        output["dor_review"] = dor.model_dump()

        impact: ImpactAssessment = self.impact.run(output)
        output["impact"] = impact.model_dump()

        integration: IntegrationCheck = self.integration.run(feature)
        output["integration"] = integration.model_dump()

        return output

    tools = [generate]
    handoffs: list = []

    def run(self, feature: str) -> Dict:
        return self.generate(feature)
