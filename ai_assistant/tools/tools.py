"""Module contains tools to be used by AI agents."""

from pydantic_ai import RunContext

# Leaving import for exposing within the package

from ai_assistant.models import Message


async def get_recent_emails(ctx: RunContext) -> list[Message]:
    """Get recent emails from the user's Gmail account."""
    return await ctx.get_tool_output("get_recent_emails")
