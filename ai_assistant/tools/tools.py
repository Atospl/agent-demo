"""Module contains tools to be used by AI agents."""

from datetime import timedelta, datetime
from zoneinfo import ZoneInfo

from ai_assistant.tools.google import CalendarClient


def get_upcoming_calendar_events() -> list[dict]:
    client = CalendarClient()
    return client.get_events(
        start_time=datetime.now(ZoneInfo("Europe/Warsaw")),
        end_time=datetime.now(ZoneInfo("Europe/Warsaw")) + timedelta(days=7),
    )
