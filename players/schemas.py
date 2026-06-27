from pydantic import BaseModel

# schema to search player
class PlayerSearchData(BaseModel):
    profile_name : str | None = None
    account_id : int | None = None
    game_id : int | None = None
    
class PlayerCreateRequest(BaseModel):
    game_id : int
    profile_name : str | None = None # If none, profile name will be account id

class PlayerUpdateData(BaseModel):
    elo: int | None = None
    profile_name : str | None = None

class PlayerResponseModel(BaseModel):
    account_id : int
    game_id : int
    profile_name : str
    elo: int

    model_config = {"from_attributes": True}