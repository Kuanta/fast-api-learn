from pydantic import BaseModel

class GameCreateData(BaseModel):
    game_code: str
    game_name: str
    game_description: str