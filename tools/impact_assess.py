class ImpactAssessmentTool:
    """Simple tool to assess impact on existing systems."""

    name = "impact_assessment"

    def __call__(self, story: dict) -> str:
        return "Minimal impact on current architecture."
