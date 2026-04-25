"""Data-access repositories — called by routes."""
from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Ticket, TicketIn


class TicketRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.s = session

    async def create(self, data: TicketIn) -> Ticket:
        # M1 planted bug territory: missing explicit commit boundary.
        # Fix is trivial once the learner notices Claude's diff didn't
        # add one. This is the subtle-bug M1.S2 asks them to find.
        t = Ticket(title=data.title, status=data.status, assignee=data.assignee)
        self.s.add(t)
        await self.s.flush()
        return t

    async def list_all(self) -> list[Ticket]:
        res = await self.s.execute(select(Ticket).order_by(Ticket.id))
        return list(res.scalars())

    async def get(self, ticket_id: int) -> Ticket | None:
        res = await self.s.execute(select(Ticket).where(Ticket.id == ticket_id))
        return res.scalar_one_or_none()
