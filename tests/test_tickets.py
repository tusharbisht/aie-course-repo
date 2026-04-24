"""Module-1 FAILING TEST: the create endpoint doesn't commit the
transaction. Learner's job (assisted by Claude) is to diagnose +
fix. This test asserts persistence across requests — the unfixed
version fails because without commit the write doesn't survive
session boundary.
"""
import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


@pytest.mark.asyncio
async def test_ticket_create_persists(client: AsyncClient) -> None:
    r = await client.post("/tickets", json={"title": "flaky login", "status": "open"})
    assert r.status_code == 201
    ticket_id = r.json()["id"]

    # Separate request — tests cross-session persistence (the bug)
    r2 = await client.get(f"/tickets/{ticket_id}")
    assert r2.status_code == 200  # ← FAILS before fix (404)
    assert r2.json()["title"] == "flaky login"
