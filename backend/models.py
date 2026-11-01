
from sqlalchemy import Column, Integer, String, JSON
from backend.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    ingredients = Column(JSON, nullable=False)
    cooking_time = Column(String, nullable=False)
    steps = Column(JSON, nullable=False)
