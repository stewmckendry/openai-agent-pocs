from pathlib import Path
from typing import Dict
from .base import BaseAgent

class DocsAgent(BaseAgent):
    def __init__(self):
        super().__init__('Docs', Path('prompts/docs.yaml'))

    def run(self, deploy_output: Dict) -> Dict:
        doc = f"## Release {deploy_output['version']}\n{deploy_output['notes']}"
        output = {'documentation': doc}
        self.record('docs', output)
        return output
