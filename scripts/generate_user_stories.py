#!/usr/bin/env python
"""CLI to generate user stories from a feature idea.

Input:
    feature: short text description of the desired feature.
Output:
    ``stories.json`` containing serialized :class:`UserStory` data along with
    ``trace.json`` and ``trace_graph.txt`` for debugging and visualization.
"""
import argparse
import asyncio
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from agents.poc_1_delivery import UserStoryLeadManager
from openai_agents.tracing import draw_graph


async def main() -> None:
    parser = argparse.ArgumentParser(description="Generate DoR user stories")
    parser.add_argument("feature", nargs="?", help="Feature summary text")
    parser.add_argument("--out", default="project/outputs", help="Output directory")
    args = parser.parse_args()

    feature = args.feature or input("Enter feature summary: ")
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

    print(typed_output.json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
