from sqlalchemy import sql, Column, Integer, String

from postgresql import db


class Agent(db.Model):
    __tablename__ = "agent"
    query: sql.Select
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Route(db.Model):
    __tablename__ = "route_sheet"
    query: sql.Select
    id = Column(Integer, Agent(id), primary_key=True)
    initial_readings = Column(Integer)
    final_readings = Column(Integer)
    difference_readings = Column(Integer, final_readings - initial_readings)
