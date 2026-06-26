from pydantic import BaseModel

class MatchCreateData(BaseModel):
    player1_id: int
    player2_id: int
    winner_id: int | None = None
    loser_id: int | None = None
    is_draw: bool = False

class MatchUpdateData(BaseModel):
    match_id: int
    winner_id: int | None = None
    loser_id: int | None = None
    is_draw: bool | None = None