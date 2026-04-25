"""STUB — Module 4 task: integrate the team-tickets MCP into /health.

The team-tickets MCP server (https://github.com/tusharbisht/aie-team-tickets-mcp)
exposes:
  - list_recent_tickets(limit: int = 10) -> list[Ticket]
  - get_ticket_health(severity: str = "high") -> {open_count, critical_ids}

YOUR TASK (M4.S3): wire these into /health so the endpoint surfaces
team ticket state alongside DB/dependency checks. The MCP is consumed
by Claude Code — but for production runtime, you'll mirror the same
data via direct calls to your team's ticket API. For this course,
mock the MCP responses by reading from a local JSON file Claude Code
generates after `claude mcp call team-tickets list_recent_tickets`.
"""
from __future__ import annotations

from pathlib import Path


def get_ticket_health_summary(snapshot_path: str = "/tmp/team-tickets-snapshot.json") -> dict:
    # TODO: read snapshot_path (created by `claude mcp call`), return summary
    # like {"open_count": N, "critical_ids": [...], "last_updated": ts}
    p = Path(snapshot_path)
    if not p.exists():
        return {"open_count": 0, "critical_ids": [], "last_updated": None, "_warning": "snapshot missing — run claude mcp call first"}
    raise NotImplementedError("M4.S3 TODO — parse snapshot_path JSON")
