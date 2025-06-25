from pathlib import Path
from typing import Dict
from .base import BaseAgent

class DevAgent(BaseAgent):
    def __init__(self):
        super().__init__('Dev', Path('prompts/dev.yaml'))

    def run(self, stories: Dict) -> Dict:
        code = "# prototype code\nprint('hello world')"
        output = {'code': code}
        self.record('develop', output)
        return output
