# module-0-preflight

## What this module teaches

M0 Preflight: run claude --version + a smoke query. Verifies your toolchain before M1.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
