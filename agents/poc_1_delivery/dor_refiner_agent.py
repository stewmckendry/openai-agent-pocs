from pathlib import Path
from typing import Dict
from .base import BaseAgent

class DoRRefinerAgent(BaseAgent):
    def __init__(self):
        super().__init__('DoRRefiner', Path('prompts/dor_refiner.yaml'))

    def run(self, stories: Dict) -> Dict:
        refined = {'stories': [{**s, 'ready': True} for s in stories.get('stories', [])]}
        self.record('refine', refined)
        return refined
