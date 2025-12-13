from google.adk.agents import LlmAgent
from .tools import get_current_time

root_agent = LlmAgent(
    name="time_agent",
    model="gemma-2-27b-it",
    instruction="""You are a helpful assistant that can tell the current date and time.
    When asked for the time, you MUST use the `get_current_time` tool.
    After the tool returns the time, you MUST explicitly tell the user what the time is.""",
    description="An agent that tells the current time.",
    tools=[get_current_time]
)
