from pathlib import Path
from typing import Dict

from .po_planner_agent import POPlannerAgent
from .po_review_agent import POReviewAgent
from .dor_refiner_agent import DoRRefinerAgent
from .dev_agent import DevAgent
from .test_agent import TestAgent
from .deploy_agent import DeployAgent
from .docs_agent import DocsAgent
from .evaluator_agent import EvaluatorAgent


class DeliveryLeadAgent:
    def __init__(self, use_search: bool = False):
        self.planner = POPlannerAgent()
        self.reviewer = POReviewAgent(use_search=use_search)
        self.evaluator = EvaluatorAgent()
        self.refiner = DoRRefinerAgent()
        self.dev = DevAgent()
        self.test = TestAgent()
        self.deploy = DeployAgent()
        self.docs = DocsAgent()
        self.trace = []

    def run(self, feature_idea: str) -> Dict:
        output = {}

        stories = self.planner.run(feature_idea)
        self.trace.extend(self.planner.trace)
        output['stories'] = stories

        review = self.reviewer.run(stories)
        self.trace.extend(self.reviewer.trace)
        output['review'] = review

        eval_result = self.evaluator.run(review)
        self.trace.extend(self.evaluator.trace)
        output['evaluation'] = eval_result
        if eval_result['needs_changes']:
            return output

        refined = self.refiner.run(stories)
        self.trace.extend(self.refiner.trace)
        output['refined'] = refined

        code = self.dev.run(refined)
        self.trace.extend(self.dev.trace)
        output['code'] = code

        test_results = self.test.run(code)
        self.trace.extend(self.test.trace)
        output['tests'] = test_results

        deploy_plan = self.deploy.run(code)
        self.trace.extend(self.deploy.trace)
        output['deploy'] = deploy_plan

        docs = self.docs.run(deploy_plan)
        self.trace.extend(self.docs.trace)
        output['docs'] = docs

        return output
