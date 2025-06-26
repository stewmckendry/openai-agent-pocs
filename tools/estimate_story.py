class StoryEstimationTool:
    """Return a fixed story point estimate."""

    name = "story_estimate"

    def __call__(self, story: dict) -> int:
        return 3
