from typing import Dict

from openai_agents.tracing import Trace, traceable

from .po_planner_agent import POPlannerAgent, PlanningOutput
from .po_review_agent import POReviewAgent, ReviewOutput
from .dor_refiner_agent import DoRRefinerAgent, RefinedStories
from .dev_agent import DevAgent, DevOutput
from .test_agent import TestAgent, TestOutput
from .deploy_agent import DeployAgent, DeployOutput
from .docs_agent import DocsAgent, DocsOutput
from .evaluator_agent import EvaluatorAgent, EvaluationOutput


class DeliveryLeadAgent:
    """Orchestrates the delivery workflow across all sub agents."""

    def __init__(self, use_search: bool = False):
        self.trace = Trace("DeliveryLead")
        self.planner = POPlannerAgent()
        self.reviewer = POReviewAgent(use_search=use_search)
        self.evaluator = EvaluatorAgent()
        self.refiner = DoRRefinerAgent()
        self.dev = DevAgent()
        self.test = TestAgent()
        self.deploy = DeployAgent()
        self.docs = DocsAgent()

    @traceable
    def run(self, feature_idea: str) -> Dict:
        output: Dict[str, object] = {}

        stories: PlanningOutput = self.planner.run(feature_idea)
        self.trace.merge(self.planner.trace)
        output["stories"] = stories.model_dump()

        review: ReviewOutput = self.reviewer.run(stories.model_dump())
        self.trace.merge(self.reviewer.trace)
        output["review"] = review.model_dump()

        evaluation: EvaluationOutput = self.evaluator.run(review)
        self.trace.merge(self.evaluator.trace)
        output["evaluation"] = evaluation.model_dump()
        if evaluation.needs_changes:
            return output

        refined: RefinedStories = self.refiner.run(stories)
        self.trace.merge(self.refiner.trace)
        output["refined"] = refined.model_dump()

        code: DevOutput = self.dev.run(refined)
        self.trace.merge(self.dev.trace)
        output["code"] = code.model_dump()

        tests: TestOutput = self.test.run(code)
        self.trace.merge(self.test.trace)
        output["tests"] = tests.model_dump()

        deploy_plan: DeployOutput = self.deploy.run(tests)
        self.trace.merge(self.deploy.trace)
        output["deploy"] = deploy_plan.model_dump()

        docs: DocsOutput = self.docs.run(deploy_plan)
        self.trace.merge(self.docs.trace)
        output["docs"] = docs.model_dump()

        return output
