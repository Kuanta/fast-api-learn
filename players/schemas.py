from pydantic import BaseModel

class PlayerSearchData(BaseModel):
    username : str
    
class PlayerCreateRequest(BaseModel):
    username : str
    password: str
    email : str

class PlayerUpdateData(BaseModel):
    rank: int | None = None

class PlayerResponseModel(BaseModel):
    id: int
    username: str
    email: str | None = None
    rank: int
    wins: int
    loses: int

class PlayerModel(BaseModel):
    id: int
    username: str
    email: str | None = None
    rank: int
    wins: int
    loses: int
    hashed_password: str

    class Config:
        orm_mode = True