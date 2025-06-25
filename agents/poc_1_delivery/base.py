"""Base class for delivery agents using the OpenAI Agents SDK."""
from pathlib import Path
from typing import Any

from openai_agents import Agent
from openai_agents.tracing import Trace, traceable


class BaseAgent(Agent):
    """Agent initialized with a prompt template and basic tracing."""

    def __init__(self, name: str, prompt_path: Path):
        instructions = Path(prompt_path).read_text()
        super().__init__(name=name, instructions=instructions)
        self.trace = Trace(name)

    def record(self, step: str, output: Any):
        """Record an event in the trace."""
        self.trace.add_event(step, output)

    @traceable
    def run(self, *args, **kwargs):
        raise NotImplementedError
