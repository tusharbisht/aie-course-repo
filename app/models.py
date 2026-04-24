"""Domain models for the user-tickets service."""
from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    status = Column(String(32), nullable=False, default="open")
    assignee = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class TicketIn(BaseModel):
    title: str
    status: str = "open"
    assignee: str | None = None


class TicketOut(BaseModel):
    id: int
    title: str
    status: str
    assignee: str | None
    created_at: datetime

    class Config:
        from_attributes = True
