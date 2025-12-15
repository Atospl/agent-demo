from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: str
    snippet: str
    sender: str
    subject: str


class CalendarEvent(BaseModel):
    summary: str
    attendees: list[str]
    start_date: datetime
    end_date: datetime
