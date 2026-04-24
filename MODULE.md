# module-6-agent-harness

## What this module teaches

M6 Agentic Coding from First Principles: build an autocorrect loop using the Anthropic SDK's tool_use, add budget + sha256 progress detection, optimize the test harness. GHA runs your harness on 3 bugs.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
