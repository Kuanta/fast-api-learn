
from games.schemas import GameCreate
from games.models import GameModel


def create_game(game_data:GameCreate):
    new_game = GameModel()
    new_game.game_code = game_data.game_code
    new_game.game_name = game_data.game_name
    new_game.game_description = game_data.game_description
    return new_game

def get_game_by_id(game_id:int):
    return GameModel.query.get(game_id)