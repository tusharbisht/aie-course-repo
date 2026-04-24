# module-1-starter

## What this module teaches

M1 First AI-Assisted Fix: failing test test_ticket_create_persists points at a bug in app/repositories.py:create. NO CLAUDE.md exists — by design. Use Claude Code to diagnose + fix.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
