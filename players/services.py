from sqlalchemy import func
from sqlalchemy.orm import Session
from players.models import PlayerModel
from players.schemas import *
from auth.utils import hash_password


def get_all_players(db: Session):
    return db.query(PlayerModel).all()

def get_player_by_username(db: Session, username: str):
    return db.query(PlayerModel).filter(func.lower(PlayerModel.username) == username.lower()).first()

def create_player(db: Session, player_data: PlayerCreateRequest):

    #Check existing player
    existing_player = get_player_by_username(db, player_data.username)
    if existing_player is not None:
        return None
    
    new_player = PlayerModel()
    #hash password
    new_player.username = player_data.username
    new_player.hashed_password = hash_password(player_data.password)
    new_player.email = player_data.email
    
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player

def update_player(db: Session, username:str, player_data: PlayerUpdateData):
    player = get_player_by_username(db, username)
    if player is not None:
        if player_data.rank is not None:
            player.rank = player_data.rank
        db.commit()
        db.refresh(player)
        return player
    else:
        return None
    
def delete_player(db: Session, username: str):
    player = get_player_by_username(db, username)
    if player is not None:
        db.delete(player)
        db.commit()
        return True
    else:
        return False