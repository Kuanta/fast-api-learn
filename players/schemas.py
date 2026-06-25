from pydantic import BaseModel

class PlayerSearchData(BaseModel):
    username : str
    
class PlayerInputData(BaseModel):
    username : str
    rank: int
    test_param: int

class PlayerUpdateData(BaseModel):
    username: str
    rank: int | None = None
    test_param: int | None = None