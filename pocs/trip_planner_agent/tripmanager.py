"""TripPlanningManager orchestrates the trip planning workflow."""

from __future__ import annotations

from rich.console import Console
from pydantic import BaseModel

from agents import Agent, Runner, trace
from agents.extensions.visualization import draw_graph

from .printer import Printer
from .agent.topic_agent import ResearchPlan, topic_agent
from .agent.research_agent import ResearchSummary, research_agent
from .agent.planner_agent import TripOutput, planner_agent

TRIP_PLANNER_PROMPT = (
    "You are a travel planner who coordinates topic generation, research, "
    "and itinerary building for a user." 
)

trip_planner_agent = Agent(
    name="TripPlannerAgent",
    instructions=TRIP_PLANNER_PROMPT,
    handoffs=[topic_agent, research_agent, planner_agent],
    output_type=TripOutput,
)


class TripPipelineOutput(BaseModel):
    """Aggregate outputs from the trip planning workflow."""

    topics: ResearchPlan
    research: list[ResearchSummary]
    plan: TripOutput


class TripPlanningManager:
    """Sequentially execute the trip planning pipeline."""

    def __init__(self, model=None) -> None:
        self.console = Console()
        self.printer = Printer(self.console)
        self.model = model
        if model is not None:
            for agent in [topic_agent, research_agent, planner_agent, trip_planner_agent]:
                agent.model = model

    async def run(self, goal: str, trace_id: str) -> TripPipelineOutput:
        try:
            with trace("trip_planner_pipeline", trace_id=trace_id):
                self.printer.update_item(
                    "trace_id",
                    f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}",
                    is_done=True,
                    hide_checkmark=True,
                )
                print(f"https://platform.openai.com/traces/trace?trace_id={trace_id}")

            with trace("topics", trace_id=trace_id):
                self.printer.update_item("topics", "Creating research topics...")
                topics_result = await Runner.run(topic_agent, goal, trace_id=trace_id)
                topics = topics_result.final_output_as(ResearchPlan)
                self.printer.update_item(
                    "topics", f"{len(topics.topics)} topics", is_done=True
                )

            research_summaries: list[ResearchSummary] = []
            with trace("research", trace_id=trace_id):
                self.printer.update_item("research", "Researching topics...")
                for item in topics.topics:
                    input_text = (
                        f"Search term: {item.query}\nReason for searching: {item.reason}"
                    )
                    result = await Runner.run(research_agent, input_text, trace_id=trace_id)
                    summary = result.final_output_as(ResearchSummary)
                    research_summaries.append(summary)
                self.printer.update_item("research", "Research complete", is_done=True)

            with trace("plan", trace_id=trace_id):
                self.printer.update_item("plan", "Drafting itinerary...")
                plan_input = (
                    f"Goal:\n{goal}\n\nTopics:\n{topics.model_dump_json()}\n\nSummaries:\n"
                    f"{[s.summary for s in research_summaries]}"
                )
                plan_result = await Runner.run(planner_agent, plan_input, trace_id=trace_id)
                plan = plan_result.final_output_as(TripOutput)
                self.printer.update_item("plan", "Itinerary ready", is_done=True)

            return TripPipelineOutput(
                topics=topics,
                research=research_summaries,
                plan=plan,
            )
        finally:
            self.printer.end()


def visualize_workflow(filename: str | None = None):
    """Generate a graphviz visualization of the workflow."""

    return draw_graph(trip_planner_agent, filename=filename)
