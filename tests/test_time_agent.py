import pytest
from agents.time_agent.agent import root_agent
from agents.time_agent.tools import get_current_time

def test_get_current_time():
    """Test that the tool returns a string."""
    time_str = get_current_time()
    assert isinstance(time_str, str)
    assert len(time_str) > 0

@pytest.mark.asyncio
async def test_agent_instantiation():
    """Test that the agent can be instantiated and has the correct tool."""
    assert root_agent.name == "time_agent"
    assert len(root_agent.tools) == 1
    assert root_agent.tools[0] == get_current_time
