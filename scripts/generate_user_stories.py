#!/usr/bin/env python
"""
CLI for generating user stories from a feature idea
Run:
  python scripts/generate_user_stories.py
  or: poetry run python scripts/generate_user_stories.py
Deployment:
  Streamlit/Gradio UI (optional), or Railway CLI
Requirements:
  - Python 3.11+
  - `openai-agents[viz]`
  - `.env` file with OPENAI_API_KEY
"""
import argparse
import asyncio
import json
from pathlib import Path
import sys
import logging

sys.path.append(str(Path(__file__).resolve().parent.parent))

from agents.poc_1_delivery.user_story_lead_manager import UserStoryLeadManager
from openai_agents.tracing import draw_graph


def setup_logging(debug: bool = False) -> None:
    level = logging.DEBUG if debug else logging.INFO
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        level=level,
        format="[%(levelname)s] [%(name)s] %(message)s",
        handlers=[logging.FileHandler("logs/agent_run.log"), logging.StreamHandler()],
    )


async def main() -> None:
    parser = argparse.ArgumentParser(description="Generate DoR user stories")
    parser.add_argument("feature", nargs="?", help="Feature summary text")
    parser.add_argument("--out", default="project/outputs", help="Output directory")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    setup_logging(args.debug)

    feature = args.feature or input("Enter feature summary: ")
    logging.getLogger(__name__).info("Generating stories for: %s", feature)
    typed_output, trace = await UserStoryLeadManager().run(feature)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "stories.json", "w") as f:
        f.write(typed_output.json(indent=2))
    with open(out_dir / "trace.json", "w") as f:
        json.dump(trace.serialize(), f, indent=2)
    with open(out_dir / "trace_graph.txt", "w") as f:
        f.write(draw_graph(trace))

    try:
        from openai_agents.visualization import visualize_trace

        visualize_trace(trace, out_dir / "trace_graph.html")
    except Exception:
        pass
    logging.getLogger(__name__).info("Output written to %s", out_dir)
    print(typed_output.json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
