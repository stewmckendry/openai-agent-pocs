from pathlib import Path
from typing import Dict
from .base import BaseAgent
from tools.web_search_tool import WebSearchTool

class POReviewAgent(BaseAgent):
    def __init__(self, use_search: bool = False):
        super().__init__('POReview', Path('prompts/po_review.yaml'))
        self.use_search = use_search
        self.search_tool = WebSearchTool() if use_search else None

    def run(self, stories: Dict) -> Dict:
        comments = 'Looks good.'
        if self.use_search:
            search_results = self.search_tool('similar features')
            comments += f' Ref: {search_results}'
        output = {'approved': True, 'comments': comments}
        self.record('review', output)
        return output
