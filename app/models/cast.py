from app.db.pg_db import Base
from sqlalchemy import Column, String, Integer

class Cast(Base):
    __tablename__='casts'
    __table_args__= {'schema': 'movies'}
    id=Column(Integer, primary_key=True)
    name=Column(String(50))
    nationality=Column(String(20))