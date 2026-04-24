"""FastAPI entrypoint."""
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session, init_db
from app.health import router as health_router
from app.models import TicketIn, TicketOut
from app.repositories import TicketRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="User Tickets", lifespan=lifespan)
app.include_router(health_router)


@app.post("/tickets", response_model=TicketOut, status_code=201)
async def create_ticket(data: TicketIn, session: AsyncSession = Depends(get_session)) -> TicketOut:
    repo = TicketRepository(session)
    t = await repo.create(data)
    return TicketOut.model_validate(t)


@app.get("/tickets", response_model=list[TicketOut])
async def list_tickets(session: AsyncSession = Depends(get_session)) -> list[TicketOut]:
    repo = TicketRepository(session)
    return [TicketOut.model_validate(t) for t in await repo.list_all()]


@app.get("/tickets/{ticket_id}", response_model=TicketOut)
async def get_ticket(ticket_id: int, session: AsyncSession = Depends(get_session)) -> TicketOut:
    repo = TicketRepository(session)
    t = await repo.get(ticket_id)
    if not t:
        raise HTTPException(404, "ticket not found")
    return TicketOut.model_validate(t)
