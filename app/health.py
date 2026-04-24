"""Health endpoint — STUB. M3 asks learner to implement this.

Module-3 task: make GET /health return {status: ok|degraded, checks: {db, redis}}
with the appropriate status codes (200 ok, 503 degraded). The schema has a
subtle gotcha — see the ticket spec in the dashboard.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    # M3 TODO: implement real health checks. This stub returns 200
    # with "unknown" — intentionally not production-ready.
    return {"status": "unknown", "checks": {}}
