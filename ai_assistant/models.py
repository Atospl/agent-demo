from pydantic import BaseModel


class Message(BaseModel):
    id: str
    snippet: str
    sender: str
    subject: str
