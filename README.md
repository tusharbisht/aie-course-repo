# AI-Augmented Engineering — Course Repo

Starter repo for Skills Lab's **AI-Augmented Engineering** course.

Fork this repo, check out the branch for each module, and follow
the dashboard's step-by-step instructions. Your Claude Code session
runs locally against this repo on your own machine.

## Branches (one per module)

| Branch | Module | Starting state |
|---|---|---|
| `module-0-preflight` | M0 Preflight | Empty baseline + verify scripts |
| `module-1-starter` | M1 First AI-Assisted Fix | One failing test, NO CLAUDE.md — intentional |
| `module-2-retry` | M2 Close Context Gap | Same as M1 + learner writes CLAUDE.md |
| `module-3-iterate` | M3 Drive 70%-Right to Done | Health endpoint stub + schema gotcha |
| `module-4-mcp` | M4 Ship w/ MCP + GHA | MCP integration entrypoint + GHA workflow primed |
| `module-5-team` | M5 Team Claude Code | `.claude/` scaffold (empty — you fill in subagents/hooks) |
| `module-6-agent-harness` | M6 Agentic Coding | Broken function + slow test suite to optimize |

## CI / Grading

`.github/workflows/lab-grade.yml` runs on push to any branch. Capstone
modules (M4, M6) instruct you to paste the Actions run URL back into
the dashboard — our backend parses the workflow's conclusion.

## Stack

- Python 3.11+
- FastAPI
- SQLite + SQLAlchemy
- pytest
