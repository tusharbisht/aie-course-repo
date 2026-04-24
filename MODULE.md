# module-4-mcp

## What this module teaches

M4 Ship w/ MCP + Review AI PR: consume the team-tickets MCP (https://github.com/tusharbisht/aie-team-tickets-mcp) — wire via `claude mcp add` + settings.json. Ship a small feature that calls the MCP. PR graded via GitHub Actions.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
