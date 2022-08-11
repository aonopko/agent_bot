
import asyncio
from .postgresql import db
from .var_for_db import POSTGRES_URI


class Agent(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_name = db.Column(db.String(255))


class Route(db.Model):
    __tablename__ = "route_sheet"
    user_id = db.Column(db.ForeignKey(f"{Agent.__tablename__}.id"))
    initial_readings = db.Column(db.Integer)
    final_readings = db.Column(db.Integer)
    value_difference = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    route = db.Column(db.String(255))


async def create_db():
    await db.set_bind(POSTGRES_URI)
    await db.gino.create_all()


loop = asyncio.get_event_loop().run_until_complete(create_db())
