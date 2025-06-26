#!/bin/bash
# Simple test runner for user_story_agent PoC

SCRIPT_DIR="$(dirname "$0")"
FEATURE_FILE="$SCRIPT_DIR/sample_input.txt"

python -m pocs.user_story_agent.main < "$FEATURE_FILE"
