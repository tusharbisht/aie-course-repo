# module-5-team

## What this module teaches

M5 Team Claude Code: write .claude/agents/test-fixer.md subagent, PreToolUse hook blocking dangerous commands, settings.json scoping permissions. Teammate-ready config.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
