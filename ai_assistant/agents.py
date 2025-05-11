from openai import AsyncOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

client = AsyncOpenAI(base_url="http://localhost:1234/v1", api_key="lm_studio")

model = OpenAIModel(model_name="qwq-32b", provider=OpenAIProvider(openai_client=client))

agent = Agent(
    model=model,
    instrument=True,
    instructions="""
You are a helpful assistant. Your goal is to create an email with a summary of the day for a user.
The email should include the following information:
- A short greeting of a user
- A summary of the day's events, taken from Google Calendar API
- A summary of the most important emails from the previous 24 hours, taken from Gmail API
- A summary of the shopping list for the next 72 hours, taken from a diet planner tool
- A weather forecast for the next 24 hours, taken from OpenWeatherMap API
- An information about events in user's place of living (if provided).
""",
)
