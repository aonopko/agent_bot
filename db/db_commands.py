from .models import Agent


async def add_agent(agent_id: int, agent_name: str):
    agent = Agent(agent_id=agent_id, agent_name=agent_name)
    await agent.create()
