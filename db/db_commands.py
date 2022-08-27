from .models import Agent


async def add_agent(agent_id: int, agent_name: str):
    agent = Agent(agent_id=agent_id, agent_name=agent_name)
    await agent.create()


async def del_agent(agent_id):
    user = await Agent.query.where(Agent.agent_id == agent_id).gino.first()
    await user.delete()


async def show_data_agent(agent_id):
    founding_users = await Agent.query.where(Agent.id == agent_id).gino.all()
    await founding_users
