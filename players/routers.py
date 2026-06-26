from fastapi import APIRouter, Query, status, HTTPException, Depends
from players.schemas import PlayerCreateRequest, PlayerUpdateData, PlayerResponseModel
from core.database import DbSession, get_db
from players import services
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/players",
    tags=["Player"] # What is this?
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PlayerResponseModel])
async def get_all_players(sort_by: str = Query(default="rank"), db: Session = Depends(get_db)):
    return services.get_all_players(db)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=PlayerResponseModel)
async def create_player(player_body: PlayerCreateRequest, db: DbSession):
    new_player = services.create_player(db, player_body)
    if new_player is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Couldn't create player")
    return new_player


@router.get("/lookup/{username}", response_model=PlayerResponseModel)
async def lookup_player(username: str, db: DbSession):
    player = services.get_player_by_username(db, username)
    if player is not None:
        return player
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

@router.put("/update/{username}", response_model=PlayerResponseModel)
async def update_player(username:str, player_body: PlayerUpdateData, db: DbSession):
    updated_player = services.update_player(db, username, player_body)
    if updated_player is not None:
        return updated_player
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
@router.delete("/delete/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(username: str, db: DbSession):
    deleted = services.delete_player(db, username)
    if deleted:
        return {"message":f"{username} has been deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")