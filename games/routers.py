from fastapi import APIRouter, status, HTTPException
from games.schemas import GameCreateData, GameUpdateData, GameResponseData
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

@router.get("/lookup/{game_id}", response_model=GameResponseData)
async def lookup_game(game_id: int, db: DbSession):
    game = services.get_game_by_id(game_id)

@router.get("/lookup/code/{game_code}", response_model=GameResponseData)
async def lookup_game(game_code: str, db: DbSession):
    game = services.get_game_by_code(game_code)

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=GameResponseData)
async def create_game(game_data: GameCreateData, admin_account: CurrentAdminAccount,db: DbSession):
    new_game = services.create_game(game_data)
    return new_game

@router.put("/update", status_code=status.HTTP_206_PARTIAL_CONTENT, response_model=GameResponseData)
async def update_game(update_data: GameUpdateData, admin_account: CurrentAdminAccount, db: DbSession):
    game = services.update_game(update_data.game_id, update_data, db)
    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return game

@router.delete("/delete/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: int, admin_account: CurrentAdminAccount, db: DbSession):
    game = services.get_game_by_id(game_id)

    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    
    has_dependents = services.game_has_dependents(game_id, db)
    if has_dependents:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Game has dependents")
    
    db.delete(game)
    db.commit()
    return None