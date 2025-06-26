"""Impact assessment agent."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent, function_tool


class ImpactSummary(BaseModel):
    summary: str


RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources"
BACKLOG_PATH = RESOURCES_DIR / "backlog.md"
AS_IS_PATH = RESOURCES_DIR / "as_is_design.md"
CODE_DIR = RESOURCES_DIR / "code"


@function_tool(name_override="read_backlog", description_override="Load the project backlog")
def read_backlog() -> str:
    return BACKLOG_PATH.read_text(encoding="utf-8")


@function_tool(name_override="read_current_design", description_override="Load the current design docs")
def read_current_design() -> str:
    return AS_IS_PATH.read_text(encoding="utf-8")


@function_tool(name_override="read_code_sample", description_override="Load a code sample file")
def read_code_sample(filename: str = "sample_module.py") -> str:
    return (CODE_DIR / filename).read_text(encoding="utf-8")


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "impact_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


impact_agent = Agent(
    name="ImpactAssessmentAgent",
    instructions=_load_prompt(),
    tools=[read_backlog, read_current_design, read_code_sample],
    output_type=ImpactSummary,
)
