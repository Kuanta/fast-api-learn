from fastapi import APIRouter, status, HTTPException
from auth.schemas import LoginResponse, LoginRequest
from core.database import DbSession
from players.services import get_player_by_username
from auth.utils import verify_password, create_access_token



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/")
async def root():
    return {"message":"Auth"}

@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(login_data: LoginRequest, db: DbSession):
    player = get_player_by_username(db, login_data.username)
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
    # Verify password
    if not verify_password(login_data.password, player.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub":player.username})
    return {"access_token":access_token, "token_type":"bearer"}
