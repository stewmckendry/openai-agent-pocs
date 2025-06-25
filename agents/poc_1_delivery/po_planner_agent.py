from pathlib import Path
from typing import List, Dict
from .base import BaseAgent

class POPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__('POPlanner', Path('prompts/po_planner.yaml'))

    def run(self, feature_idea: str) -> Dict:
        stories = []
        for i, idea in enumerate(feature_idea.split('\n')[:3], start=1):
            stories.append({'id': f'STORY-{i}', 'title': idea.strip(), 'description': idea.strip()})
        output = {'stories': stories}
        self.record('plan', output)
        return output
