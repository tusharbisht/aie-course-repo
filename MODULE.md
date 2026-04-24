# module-3-iterate

## What this module teaches

M3 Drive 70%-right to done: add a /health endpoint that checks DB + Redis. Repo has a subtle schema gotcha Claude will miss on the first attempt. Rewrite your PROMPT, don't argue with Claude's output.

## Task

See the dashboard step for the full task spec, rubric, and submission format.
Dashboard: http://localhost:8001/#created-7fee8b78c742

## Running tests

```
pip install -r requirements.txt
pytest -v
```

CI runs on every push via `.github/workflows/lab-grade.yml` — capstone modules use the run URL as the graded artifact.
