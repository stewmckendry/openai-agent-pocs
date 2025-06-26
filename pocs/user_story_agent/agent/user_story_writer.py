"""User story writer agent.

This agent combines functional and technical specifications into a final
user story document. The prompt text is loaded from
``prompts/user_story_writer.yaml``. The agent exposes a simple tool
``write_user_story`` that can be called by the model to format the
output.
"""

from pathlib import Path
from pydantic import BaseModel

from agents import Agent, function_tool


class UserStory(BaseModel):
    """Structured output containing the final user story."""

    story: str


@function_tool(
    name_override="write_user_story",
    description_override="Combine functional and technical specs into a final user story",
)
def write_user_story(functional: str, technical: str) -> str:
    """Return a markdown user story from the given specs."""
    return f"## Functional Specification\n{functional}\n\n## Technical Specification\n{technical}"


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "user_story_writer.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


user_story_writer_agent = Agent(
    name="UserStoryWriterAgent",
    instructions=_load_prompt(),
    tools=[write_user_story],
    output_type=UserStory,
)
