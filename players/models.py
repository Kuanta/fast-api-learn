from core.database import Base
from sqlalchemy import Column, Integer, String

class PlayerModel(Base):
    __tablename__ = "players"

    # Kolon tanımlamaları
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    rank = Column(Integer,default=0, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    wins = Column(Integer, default=0, nullable=False)
    loses = Column(Integer, default=0, nullable=False)
