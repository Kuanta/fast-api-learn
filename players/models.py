from core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class PlayerModel(Base):
    __tablename__ = "players"

    # Kolon tanımlamaları
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    wins = Column(Integer, default=0, nullable=False)
    loses = Column(Integer, default=0, nullable=False)