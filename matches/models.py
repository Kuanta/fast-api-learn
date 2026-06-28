from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from core.database import Base


class MatchModel(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"), index=True, nullable=False)
    winner_faction = Column(Integer, nullable=True)
    is_draw = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    game = relationship("GameModel", back_populates="matches")
    participants = relationship("MatchParticipantModel", back_populates="match", cascade="all, delete-orphan")


class MatchParticipantModel(Base):
    __tablename__ = "match_participants"
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"), index=True, nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), index=True, nullable=False)
    faction_id = Column(Integer, nullable=False)
    match = relationship("MatchModel", back_populates="participants")
    account = relationship("AccountModel")