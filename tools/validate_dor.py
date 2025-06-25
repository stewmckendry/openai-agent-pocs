class ValidateDoR:
    """Custom tool to check if a story meets Definition of Ready (DoR)."""
    name = "validate_DoR"

    def __call__(self, story: dict) -> bool:
        required_fields = ["id", "title", "description"]
        return all(story.get(f) for f in required_fields)
