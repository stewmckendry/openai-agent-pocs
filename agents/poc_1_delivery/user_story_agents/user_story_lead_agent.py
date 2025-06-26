from typing import Dict

from openai_agents.tracing import Trace, traceable, draw_graph

from .ux_spec_agent import UXSpecAgent, UXSpec
from .functionality_agent import FunctionalityAgent, FunctionalitySpec
from .tech_spec_agent import TechSpecAgent, TechSpec
from .acceptance_agent import AcceptanceCriteriaAgent, AcceptanceCriteria
from .story_estimation_agent import StoryEstimationAgent, StoryEstimate
from .dor_review_agent import DoRReviewAgent, DoRReview
from .impact_assessment_agent import ImpactAssessmentAgent, ImpactAssessment
from .tech_context_agent import TechContextAgent, TechContext
from .integration_check_agent import IntegrationCheckAgent, IntegrationCheck


class UserStoryLeadAgent:
    """Generate Definition of Ready user stories from a feature description."""

    def __init__(self):
        self.trace = Trace("UserStoryLead")
        self.ux = UXSpecAgent()
        self.func = FunctionalityAgent()
        self.tech = TechSpecAgent()
        self.acceptance = AcceptanceCriteriaAgent()
        self.estimate = StoryEstimationAgent()
        self.dor = DoRReviewAgent()
        self.impact = ImpactAssessmentAgent()
        self.context = TechContextAgent()
        self.integration = IntegrationCheckAgent()

    @traceable
    def run(self, feature: str) -> Dict:
        output: Dict[str, Dict] = {}

        context: TechContext = self.context.run()
        self.trace.merge(self.context.trace)
        output["tech_context"] = context.model_dump()

        ux: UXSpec = self.ux.run(feature)
        self.trace.merge(self.ux.trace)
        output["ux"] = ux.model_dump()

        functionality: FunctionalitySpec = self.func.run(feature)
        self.trace.merge(self.func.trace)
        output["functionality"] = functionality.model_dump()

        tech: TechSpec = self.tech.run(feature)
        self.trace.merge(self.tech.trace)
        output["tech_spec"] = tech.model_dump()

        acceptance: AcceptanceCriteria = self.acceptance.run(feature)
        self.trace.merge(self.acceptance.trace)
        output["acceptance"] = acceptance.model_dump()

        estimate: StoryEstimate = self.estimate.run(feature)
        self.trace.merge(self.estimate.trace)
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
        self.trace.merge(self.dor.trace)
        output["dor_review"] = dor.model_dump()

        impact: ImpactAssessment = self.impact.run(output)
        self.trace.merge(self.impact.trace)
        output["impact"] = impact.model_dump()

        integration: IntegrationCheck = self.integration.run(feature)
        self.trace.merge(self.integration.trace)
        output["integration"] = integration.model_dump()

        self.trace.add_event("graph", draw_graph(self.trace))
        return output
