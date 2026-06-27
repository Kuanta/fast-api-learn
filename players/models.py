from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship
from core.database import Base


class PlayerModel(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), index=True, nullable=False)
    game_id = Column(Integer, ForeignKey("games.id"), index=True, nullable=False)
    profile_name = Column(String, nullable=False)
    elo = Column(Integer, default=0, nullable=False)
    wins = Column(Integer, default=0, nullable=False)
    loses = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    account = relationship("AccountModel", back_populates="players")
    game = relationship("GameModel", back_populates="players")

    __table_args__ = (
        # Bir hesabın bir oyunda en fazla bir profili olabilir
        UniqueConstraint("account_id", "game_id", name="uq_player_account_game"),
        # Profil adları oyun içinde benzersiz (farklı oyunlarda aynı ad olabilir)
        UniqueConstraint("game_id", "profile_name", name="uq_player_game_profile_name"),
    )
