"""RunCoachManager orchestrates the run coaching workflow."""

from datetime import datetime
from rich.console import Console
from pydantic import BaseModel

from agents import Agent
from agents import Runner, trace
from agents.extensions.visualization import draw_graph

from .printer import Printer
from .agent.goal_agent import RaceGoal, goal_agent
from .agent.collect_agent import RunData, collect_agent
from .agent.analyze_agent import StatsAnalysis, analyze_agent
from .agent.plan_agent import RacePlan, plan_agent
from .agent.check_agent import check_agent


RUN_COACH_PROMPT = (
    "You are a virtual running coach who coordinates goal setting, stats "
    "collection, analysis and planning to help a runner prepare for their race."
)


run_coach_agent = Agent(
    name="RunCoachAgent",
    instructions=RUN_COACH_PROMPT,
    handoffs=[goal_agent, collect_agent, analyze_agent, plan_agent, check_agent],
    output_type=RacePlan,
)


class RunCoachPipelineOutput(BaseModel):
    """Aggregate outputs from the run coach pipeline."""

    goal: RaceGoal
    runs: RunData
    analysis: StatsAnalysis
    plan: RacePlan


class RunCoachManager:
    """Sequentially execute the run coach pipeline."""

    def __init__(self, model=None) -> None:
        self.console = Console()
        self.printer = Printer(self.console)
        self.model = model
        if model is not None:
            for agent in [
                goal_agent,
                collect_agent,
                analyze_agent,
                plan_agent,
                check_agent,
                run_coach_agent,
            ]:
                agent.model = model

    async def run(self, goal_description: str, trace_id: str) -> RunCoachPipelineOutput:
        with trace("run_coach_pipeline", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}",
                is_done=True,
                hide_checkmark=True,
            )
            print(f"https://platform.openai.com/traces/trace?trace_id={trace_id}")

            current_date = datetime.now().date().isoformat()

            with trace("goal", trace_id=trace_id):
                self.printer.update_item("goal", "Parsing goal...")
                goal_input = f"current_date: {current_date}\nuser_input: {goal_description}"
                goal_result = await Runner.run(goal_agent, goal_input, trace_id=trace_id)
                goal = goal_result.final_output_as(RaceGoal)
                self.printer.update_item("goal", str(goal), is_done=True)

            with trace("collect", trace_id=trace_id):
                self.printer.update_item("collect", "Loading runs...")
                collect_result = await Runner.run(collect_agent, "load", trace_id=trace_id)
                runs = collect_result.final_output_as(RunData)
                self.printer.update_item("collect", "Runs loaded", is_done=True)

            with trace("analyze", trace_id=trace_id):
                self.printer.update_item("analyze", "Analyzing runs...")
                analyze_input = (
                    f"Goal:\n{goal.model_dump_json()}\n\nRuns CSV:\n{runs.csv}"
                )
                analyze_result = await Runner.run(analyze_agent, analyze_input, trace_id=trace_id)
                analysis = analyze_result.final_output_as(StatsAnalysis)
                self.printer.update_item("analyze", "Analysis complete", is_done=True)

            with trace("plan", trace_id=trace_id):
                self.printer.update_item("plan", "Drafting plan...")
                plan_input = (
                    f"Goal:\n{goal.model_dump_json()}\n\nAnalysis:\n{analysis.analysis}"
                )
                plan_result = await Runner.run(plan_agent, plan_input, trace_id=trace_id)
                plan = plan_result.final_output_as(RacePlan)
                self.printer.update_item("plan", "Plan drafted", is_done=True)

            with trace("check", trace_id=trace_id):
                self.printer.update_item("check", "Checking plan...")
                check_result = await Runner.run(check_agent, plan.plan, trace_id=trace_id)
                final_plan = check_result.final_output_as(RacePlan)
                self.printer.update_item("check", "Plan checked", is_done=True)

            self.printer.end()
            return RunCoachPipelineOutput(
                goal=goal,
                runs=runs,
                analysis=analysis,
                plan=final_plan,
            )


def visualize_workflow(filename: str | None = None):
    """Generate a graphviz visualization of the workflow."""

    return draw_graph(run_coach_agent, filename=filename)
