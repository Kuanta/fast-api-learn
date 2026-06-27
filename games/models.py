from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from core.database import Base


class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Bir oyun -> birden çok oyuncu profili ve maç
    players = relationship("PlayerModel", back_populates="game")
    matches = relationship("MatchModel", back_populates="game")
