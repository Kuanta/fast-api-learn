from pydantic import BaseModel

class MatchParticipantData(BaseModel):
    account_id: int
    faction_id : int

    model_config = {"from_attributes": True}

class MatchData(BaseModel):
    winner_faction: int | None = None
    game_id: int
    participants: list[MatchParticipantData]

    model_config = {"from_attributes": True}


