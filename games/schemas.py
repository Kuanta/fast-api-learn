from pydantic import BaseModel

class GameCreateData(BaseModel):
    game_code: str
    game_name: str
    game_description: str

class GameUpdateData(BaseModel):
    game_code: str | None = None
    game_name: str | None = None
    game_description: str | None = None

class GameResponseData(BaseModel):
    game_id: int
    game_code: str
    game_name: str
    game_description: str

    model_config = {"from_attributes": True}