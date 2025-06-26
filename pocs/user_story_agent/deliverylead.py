"""Delivery Lead agent and helpers.

This module orchestrates the user story workflow by running three
sub-agents sequentially: ``functional_agent``, ``technical_agent``, and
``user_story_writer_agent``. The final output is a full user story
produced by ``user_story_writer_agent``.
"""

from __future__ import annotations

from rich.console import Console

from agents import Agent, Runner, trace
from agents.extensions.visualization import draw_graph

from .agent.functional_agent import FunctionalSpec, functional_agent
from .agent.technical_agent import TechnicalSpec, technical_agent
from .agent.user_story_writer import UserStory, user_story_writer_agent
from .printer import Printer


DELIVERY_PROMPT = (
    "You are a software delivery lead. When given a feature description, "
    "first delegate to the FunctionalSpecAgent to produce a functional "
    "specification. Then delegate to the TechnicalSpecAgent to convert that "
    "functional spec into a technical specification. Finally delegate to the "
    "UserStoryWriterAgent to produce the final user story document."
)


# Agent object used only for workflow visualization
delivery_lead_agent = Agent(
    name="DeliveryLeadAgent",
    instructions=DELIVERY_PROMPT,
    handoffs=[functional_agent, technical_agent, user_story_writer_agent],
    output_type=UserStory,
)


class DeliveryLeadManager:
    """Orchestrates the sequential user story generation workflow."""

    def __init__(self) -> None:
        self.console = Console()
        self.printer = Printer(self.console)

    async def run(self, feature: str) -> UserStory:
        with trace("functional_spec"):
            self.printer.update_item("functional", "Generating functional spec...")
            func_result = await Runner.run(functional_agent, feature)
            functional = func_result.final_output_as(FunctionalSpec)
            self.printer.update_item("functional", functional.spec, is_done=True)

        with trace("technical_spec"):
            self.printer.update_item("technical", "Generating technical spec...")
            tech_result = await Runner.run(technical_agent, functional.spec)
            technical = tech_result.final_output_as(TechnicalSpec)
            self.printer.update_item("technical", technical.spec, is_done=True)

        with trace("user_story"):
            self.printer.update_item("story", "Writing user story...")
            input_data = (
                f"Functional specification:\n{functional.spec}\n\n"
                f"Technical specification:\n{technical.spec}"
            )
            story_result = await Runner.run(user_story_writer_agent, input_data)
            story = story_result.final_output_as(UserStory)
            self.printer.update_item("story", "User story complete", is_done=True)
            self.printer.end()
            return story


def visualize_workflow(filename: str | None = None):
    """Generate a graphviz visualization of the agent workflow."""

    return draw_graph(delivery_lead_agent, filename=filename)
