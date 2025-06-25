from pathlib import Path
from typing import Dict
from .base import BaseAgent

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__('Evaluator', Path('prompts/evaluator.yaml'))

    def run(self, stage_output: Dict) -> Dict:
        needs_changes = False
        if isinstance(stage_output, dict) and 'approved' in stage_output:
            needs_changes = not stage_output.get('approved', True)
        output = {'needs_changes': needs_changes}
        self.record('evaluate', output)
        return output
