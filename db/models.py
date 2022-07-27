from sqlalchemy import sql, Column, Integer
from postgresql import db


class Route(db.Model):
    __tablename__ = "route_sheet"
    query: sql.Select
    id = Column(Integer, primary_key=True)
    initial_readings = Column(Integer)
    final_readings = Column(Integer)

    query: sql.Select
