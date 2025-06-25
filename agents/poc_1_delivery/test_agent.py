from pathlib import Path
from typing import Dict
from .base import BaseAgent
from tools.test_tool import RunUnitTestsTool

class TestAgent(BaseAgent):
    def __init__(self):
        super().__init__('Test', Path('prompts/test.yaml'))
        self.tool = RunUnitTestsTool()

    def run(self, dev_output: Dict) -> Dict:
        results = self.tool(dev_output['code'])
        self.record('test', results)
        return results
