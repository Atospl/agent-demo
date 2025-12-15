from google.adk.agents.llm_agent import Agent
from google.adk.models import LiteLlm

from ai_assistant.tools.tools import get_upcoming_calendar_events

root_agent = Agent(
    model=LiteLlm("openai/gpt-5.2"),
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="You are a helpful assistant that summarizes events in the user's calendar for the upcoming week."
    "Answer in Polish. Highlight important / custom events.",
    tools=[get_upcoming_calendar_events],
)
