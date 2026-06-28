
from sqlalchemy.orm import Session

from games.schemas import GameCreateData, GameUpdateData
from games.models import GameModel
from players.models import PlayerModel
from matches.models import MatchModel


def create_game(game_data:GameCreateData, db:Session):
    new_game = GameModel()
    new_game.game_code = game_data.game_code
    new_game.game_name = game_data.game_name
    new_game.game_description = game_data.game_description
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

def get_game_by_id(game_id:int, db: Session):
    return db.query(GameModel).filter(GameModel.id == game_id).first()

def get_game_by_code(game_code:str, db:Session):
    return db.query(GameModel).filter(GameModel.game_code == game_code).first()

def game_has_dependents(game_id: int, db: Session) -> bool:
    """Return True if any player profile or match still references this game.

    Used to block deletion of a game that is still in use, so we never
    orphan players/matches that point at it through their game_id.
    """
    has_players = db.query(PlayerModel).filter(PlayerModel.game_id == game_id).first() is not None
    if has_players:
        return True
    return db.query(MatchModel).filter(MatchModel.game_id == game_id).first() is not None

def update_game(game_id:int, update_data: GameUpdateData, db:Session):
    game = get_game_by_id(game_id, db)
    if game is None:
        return None
    
    # Update fields
    if update_data.game_code is not None:
        game.game_code = update_data.game_code
    if update_data.game_name is not None:
        game.game_name = update_data.game_name
    if update_data.game_description is not None:
        game.game_description = update_data.game_description

    # save changes to db
    db.commit()
    db.refresh(game)
    return game


def delete_game(game_id: int, db: Session):
    game = get_game_by_id(game_id, db)
    if game is None:
        return None

    db.delete(game)
    db.commit()
    return game

