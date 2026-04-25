<<<<<<< HEAD
# module-6-agent-harness

## What this module teaches

M6 Agentic Coding from First Principles: build an autocorrect loop using the Anthropic SDK's tool_use, add budget + sha256 progress detection, optimize the test harness. GHA runs your harness on 3 bugs.
=======
<<<<<<< HEAD
# module-5-team

## What this module teaches

M5 Team Claude Code: write .claude/agents/test-fixer.md subagent, PreToolUse hook blocking dangerous commands, settings.json scoping permissions. Teammate-ready config.
=======
# module-4-mcp

## What this module teaches

M4 Ship w/ MCP + Review AI PR: consume the team-tickets MCP (https://github.com/tusharbisht/aie-team-tickets-mcp) — wire via `claude mcp add` + settings.json. Ship a small feature that calls the MCP. PR graded via GitHub Actions.
>>>>>>> module-4-mcp
>>>>>>> module-5-team

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
