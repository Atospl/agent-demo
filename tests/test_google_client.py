"""Unit tests for gmail client module."""

from datetime import datetime, timedelta, timezone

import pytest

from ai_assistant.tools.google import GmailClient, CalendarClient


@pytest.fixture
def gmail_client() -> GmailClient:
    return GmailClient()


@pytest.fixture
def calendar_client() -> CalendarClient:
    return CalendarClient()


def test_00_authenticate(gmail_client: GmailClient):
    results = gmail_client.service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])
    assert results is not None
    assert len(labels) > 0


def test_01_get_messages(gmail_client: GmailClient):
    messages = gmail_client.get_last_messages()
    assert len(messages) > 0


def test_02_get_calendar_events(calendar_client: CalendarClient):
    events = calendar_client.get_events(
        start_time=datetime.now(tz=timezone.utc),
        end_time=datetime.now(tz=timezone.utc) + timedelta(days=1),
    )
    assert len(events) > 0
