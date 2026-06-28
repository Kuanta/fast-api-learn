from fastapi import APIRouter, status, HTTPException
from auth.schemas import LoginResponse, LoginRequest, AccountResponse, RegisterRequest
from core.database import DbSession
from auth.services import get_account_by_username, create_account
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
    account = get_account_by_username(login_data.username, db)
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Account not found")
    
    # Verify password
    if not verify_password(login_data.password, account.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub":account.username})
    return {"access_token":access_token, "token_type":"bearer"}

@router.post("/register",response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def register(register_data: RegisterRequest, db: DbSession):
    existing_account = get_account_by_username(register_data.username, db)
    if existing_account:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    
    account = create_account(register_data, db)
    return account
