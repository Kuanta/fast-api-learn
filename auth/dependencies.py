from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.database import DbSession
from core.config import settings
from auth.services import get_account_by_username
from auth.models import AccountModel

from auth.utils import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_account(token: Annotated[str, Depends(oauth2_scheme)], db: DbSession):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    username = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    account = get_account_by_username(username, db)
    if account is None:
        raise credentials_exception

    return account

CurrentAccount = Annotated[AccountModel, Depends(get_current_account)]

def require_role_level(min_role_level:int):
    def checker(current_account: CurrentAccount):
        if current_account.account_level < min_role_level:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Low account level")
        return current_account
    return checker


CurrentAdminAccount = Annotated[AccountModel, Depends(require_role_level(settings.ADMIN_ROLE_LEVEL))]