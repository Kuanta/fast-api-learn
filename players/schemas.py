from pydantic import BaseModel

# schema to search player
class PlayerSearchData(BaseModel):
    profile_name : str | None = None
    account_id : str | None = None
    game_id : str | None = None
    
class PlayerCreateRequest(BaseModel):
    game_id : str
    profile_name : str | None = None # If none, profile name will be account id

class PlayerUpdateData(BaseModel):
    rank: int | None = None
    profile_name : str | None = None

class PlayerResponseModel(BaseModel):
    account_id : str
    game_id : str
    profile_name : str
    rank: int
