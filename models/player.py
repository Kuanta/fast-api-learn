from dataclasses import dataclass
from pydantic import BaseModel



class Player:
    def __init__(self, username:str, rank: int, test_param:int = 0):
        self.username = username
        self.rank = rank
        self.test_param = test_param

class PlayerInputData(BaseModel):
    username : str
    rank: int
    test_param: int

class PlayerUpdateData(BaseModel):
    username: str
    rank: int | None = None
    test_param: int | None = None