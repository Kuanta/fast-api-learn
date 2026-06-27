from pydantic import BaseModel

class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str
    
class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

class AccountResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    account_level: int
    model_config = {
        "from_attributes": True
    }
