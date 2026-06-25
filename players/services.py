from sqlalchemy.orm import Session
from players.models import PlayerModel
from players.schemas import *

def get_all_players(db: Session):
    return db.query(PlayerModel).all()

def get_player_by_username(db: Session, username: str):
    return db.query(PlayerModel).filter(PlayerModel.username.lower == username.lower)

def create_player(db: Session, player_data: PlayerInputData):
    new_player = PlayerModel(username=player_data.username)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player