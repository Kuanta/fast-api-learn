from fastapi import APIRouter, Query, status, HTTPException, Depends
from players.schemas import PlayerCreateRequest, PlayerUpdateData, PlayerResponseModel
from core.database import DbSession, get_db
from players import services
from sqlalchemy.orm import Session
from auth.dependencies import CurrentAccount

router = APIRouter(
    prefix="/players",
    tags=["Player"] # What is this?
)

# GET REQUESTS
@router.get("/me", response_model=list[PlayerResponseModel])
async def get_current_player(current_account: CurrentAccount, db: DbSession):
    return services.get_all_account_profiles(current_account.id, db)


@router.get("/me/{game_id}", response_model=PlayerResponseModel)
async def get_current_player_game_profile(game_id: str, current_account: CurrentAccount, db: DbSession):
    current_player = services.get_game_profile(game_id, current_account.id, db)

    return current_player

@router.get("/games/{game_id}",response_model=list[PlayerResponseModel])
async def get_all_profiles(game_id: str, db: DbSession):
    return services.get_all_profiles(game_id, db)

@router.get("/games/{game_id}/{user_id}")
async def get_game_profile(game_id: str, user_id: str, db: DbSession):
    return services.get_game_profile(game_id, user_id, db)
    
# POST REQUESTS
@router.post("/create}", status_code=status.HTTP_201_CREATED, response_model=PlayerResponseModel)
async def create_player(player_body: PlayerCreateRequest, current_account: CurrentAccount, db: DbSession):
    new_player = services.create_profile(player_body, db)
    if new_player is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Couldn't create player")
    return new_player

@router.put("/update/{username}", response_model=PlayerResponseModel)
async def update_player(username:str, player_body: PlayerUpdateData, db: DbSession):
    updated_player = services.update_profile(db, username, player_body)
    if updated_player is not None:
        return updated_player
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
@router.delete("/delete/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(username: str, db: DbSession):
    deleted = services.delete_profile(db, username)
    if deleted:
        return {"message":f"{username} has been deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")