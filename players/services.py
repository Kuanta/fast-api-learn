from sqlalchemy import func
from sqlalchemy.orm import Session
from players.models import PlayerModel
from players.schemas import *

def get_all_profiles(game_id:str, db: Session):
    return db.query(PlayerModel).filter(PlayerModel.game_id == game_id).all()

def get_all_account_profiles(account_id:str, db: Session):
    return db.query(PlayerModel).filter(PlayerModel.account_id == account_id).all()

def get_game_profile(game_id:str, account_id:str, db: Session):
    '''
    Gets game profile for given game_id and account_id
    '''
    return db.query(PlayerModel).filter(PlayerModel.game_id == game_id, PlayerModel.account_id == account_id).first()

def create_profile(profile_data: PlayerCreateRequest, account_id:int, db: Session):

    #Check existing player
    existing_player = get_game_profile(profile_data.game_id, account_id, db)
    if existing_player is not None:
        return None
    
    new_player = PlayerModel()
    new_player.account_id = account_id
    new_player.game_id = profile_data.game_id
    new_player.profile_name = profile_data.profile_name if profile_data.profile_name is not None else account_id
    new_player.elo = 0
    
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player

def update_profile(account_id: int, game_id: int, player_data: PlayerUpdateData, db: Session) -> PlayerModel | None:
    player = get_game_profile(game_id, account_id, db)
    if player is not None:
        if player_data.elo is not None:
            player.elo = player_data.elo
        if player_data.profile_name is not None:
            player.profile_name = player_data.profile_name
        db.commit()
        db.refresh(player)
        return player
    else:
        return None
    
def increase_win(account_id, game_id, db: Session):
    profile = get_game_profile(game_id, account_id, db)
    if profile is not None:
        profile.wins += 1
    return profile

def increase_lose(account_id, game_id, db: Session):
    profile = get_game_profile(game_id, account_id, db)
    if profile is not None:
        profile.loses += 1
    return profile
    
def delete_profile(account_id: str, game_id: str, db: Session) -> PlayerModel | None:
    player = get_game_profile(game_id, account_id, db)
    if player is not None:
        db.delete(player)
        db.commit()
        return player
    else:
        return None