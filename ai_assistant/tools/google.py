"""Contains code for GMAIL client"""

from datetime import datetime, timedelta
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ai_assistant.models import Message


def authenticate_google(scopes_requested: list[str]) -> Credentials:
    creds = None

    if os.path.exists("token.json"):
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file(
                "token.json", scopes_requested
            )
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", scopes_requested
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


class GmailClient:
    """Gmail client."""

    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        self.__creds = authenticate_google(scopes_requested=self.SCOPES)
        self.service = build("gmail", "v1", credentials=self.__creds)

    def get_last_messages(self) -> list[Message]:
        """Returns messages from the last 24 hours."""
        try:
            message_ids = (
                self.service.users()
                .messages()
                .list(
                    userId="me",
                    q=f"after:{(datetime.now() - timedelta(days=1)).strftime('%Y/%m/%d')}",
                    maxResults=30,
                )
                .execute()["messages"]
            )
            messages = []
            for message_id in message_ids:
                message = (
                    self.service.users()
                    .messages()
                    .get(userId="me", id=message_id["id"])
                    .execute()
                )
                message["sender"] = next(
                    filter(
                        lambda header: header["name"] == "From",
                        message["payload"]["headers"],
                    )
                )["value"]
                message["subject"] = next(
                    filter(
                        lambda header: header["name"] == "Subject",
                        message["payload"]["headers"],
                    )
                )["value"]
                messages.append(message)
            return [Message(**message) for message in messages]
        except HttpError as error:
            print(f"An error occurred: {error}")


class CalendarClient:
    """Google Calendar client."""

    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
        self.__creds = authenticate_google(scopes_requested=self.SCOPES)
        self.service = build("calendar", "v3", credentials=self.__creds)

    def get_events(self, start_time: datetime, end_time: datetime) -> list[Message]:
        """Returns events between start_time and end_time."""
        try:
            events_result = (
                self.service.events()
                .list(
                    calendarId="primary",
                    timeMin=start_time.isoformat(),
                    timeMax=end_time.isoformat(),
                    maxResults=30,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])
            return events
        except HttpError as error:
            print(f"An error occurred: {error}")
