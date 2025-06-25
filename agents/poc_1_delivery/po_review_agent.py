from pathlib import Path
from typing import Dict

import openai
from pydantic import BaseModel

from openai_agents.tracing import traceable
from openai_agents.tools import OpenAITool

from .base import BaseAgent
from tools.web_search_tool import WebSearchTool


class WebSearch(OpenAITool):
    """OpenAI tool wrapper around the local WebSearchTool."""

    def __init__(self):
        super().__init__(name="web_search")
        self.tool = WebSearchTool()

    def run(self, query: str) -> str:  # noqa: D401
        return self.tool(query)


class ReviewOutput(BaseModel):
    approved: bool
    comments: str


class POReviewAgent(BaseAgent):
    def __init__(self, use_search: bool = False):
        super().__init__("POReview", Path("prompts/po_review.yaml"))
        self.use_search = use_search
        self.search_tool = WebSearch() if use_search else None

    @traceable
    def run(self, stories: Dict) -> ReviewOutput:
        """Review stories for alignment, optionally using web search."""
        context = stories
        search_ref = ""
        if self.search_tool:
            search_ref = self.search_tool.run("similar features")
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": str(context)},
                {"role": "system", "content": search_ref},
            ],
        )
        content = response.choices[0].message.content
        approved = "approved" in content.lower()
        output = ReviewOutput(approved=approved, comments=content)
        self.record("review", output.model_dump())
        return output
