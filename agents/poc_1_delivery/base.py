import json
from pathlib import Path
from typing import Dict, Any


class BaseAgent:
    """Simple agent that loads a prompt and produces templated output."""

    def __init__(self, name: str, prompt_path: Path):
        self.name = name
        with open(prompt_path) as f:
            content = f.read()
        # very naive YAML parsing for `prompt:` key
        if content.startswith('prompt:'):
            self.prompt = content.split('\n', 1)[1].lstrip()
        else:
            self.prompt = content
        self.trace = []

    def record(self, step: str, output: Any):
        self.trace.append({'step': step, 'output': output})

    def save_output(self, path: Path, output: Any):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(output, f, indent=2)

    def run(self, *args, **kwargs):
        raise NotImplementedError
