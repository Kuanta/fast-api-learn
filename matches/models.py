from core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class MatchModel(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(Integer, nullable=False)
    player2_id = Column(Integer, nullable=False)
    winner_id = Column(Integer, nullable=True)
    loser_id = Column(Integer, nullable=True)
    is_draw = Column(Boolean, default=False, nullable=False)