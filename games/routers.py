from fastapi import APIRouter, status, HTTPException
from games.schemas import GameCreateData, GameResponseData
from core.database import DbSession, get_db
from auth.dependencies import CurrentAdminAccount
from games import services

router = APIRouter(
    prefix = "/games",
    tags = ["Games"]
)

@router.get("/")
async def games_root():
    return {"message":"Games API"}

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=GameResponseData)
async def create_game(game_data: GameCreateData, admin_account: CurrentAdminAccount,db: DbSession):
    new_game = services.create_game(game_data)
    return new_game

@router.delete("/delete/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: int, admin_account: CurrentAdminAccount, db: DbSession):
    game = services.get_game_by_id(game_id)
    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    db.delete(game)
    db.commit()
    return None