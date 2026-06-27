from sqlalchemy import func
from sqlalchemy.orm import Session
from auth.models import AccountModel
from auth.schemas import RegisterRequest
from auth.utils import hash_password


def get_account_by_id(id:str, db:Session):
    return db.query(AccountModel).filter(AccountModel.id == id).first()

def get_account_by_username(username:str, db:Session):
    return db.query(AccountModel).filter(AccountModel.username == username).first()

def create_account(register_data: RegisterRequest, db:Session):
    new_account = AccountModel()
    new_account.email = register_data.email
    new_account.username = register_data.username
    new_account.hashed_password = hash_password(register_data.password)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account