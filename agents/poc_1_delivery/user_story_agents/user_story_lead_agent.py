from typing import Dict

from openai_agents import Agent
from openai_agents.tools import tool

from .ux_spec_agent import UXSpecAgent
from .functionality_agent import FunctionalityAgent
from .tech_spec_agent import TechSpecAgent
from .acceptance_agent import AcceptanceCriteriaAgent
from .story_estimation_agent import StoryEstimationAgent
from .dor_review_agent import DoRReviewAgent
from .impact_assessment_agent import ImpactAssessmentAgent
from .tech_context_agent import TechContextAgent
from .integration_check_agent import IntegrationCheckAgent


class UserStoryLeadAgent(Agent):
    """Generate Definition of Ready user stories from a feature description."""

    def __init__(self):
        instructions = "Generate Definition of Ready user stories from a feature description."
        # Instantiate sub-agents in reverse order so we can wire handoffs
        self.integration = IntegrationCheckAgent()
        self.impact = ImpactAssessmentAgent(next_agent=self.integration)
        self.dor = DoRReviewAgent(next_agent=self.impact)
        self.estimate = StoryEstimationAgent(next_agent=self.dor)
        self.acceptance = AcceptanceCriteriaAgent(next_agent=self.estimate)
        self.tech = TechSpecAgent(next_agent=self.acceptance)
        self.func = FunctionalityAgent(next_agent=self.tech)
        self.ux = UXSpecAgent(next_agent=self.func)
        self.context = TechContextAgent(next_agent=self.ux)

        super().__init__(
            name="UserStoryLead",
            instructions=instructions,
            tools=[self.generate],
            handoffs=[self.context],
        )

    @tool
    def generate(self, feature: str) -> Dict:
        """Entrypoint for the user story workflow."""
        return {"feature": feature}

    tools = [generate]
