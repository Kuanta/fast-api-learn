from core.database import session_local
from auth.models import AccountModel
from auth.services import get_account_by_username
from auth.utils import hash_password
from core.config import settings
import argparse

# Tüm modelleri SQLAlchemy registry'sine kaydet ki ilişkiler ("PlayerModel" gibi
# string referanslar) çözülebilsin. Script main.py'dan geçmediği için elle import.
import auth.models, players.models, games.models, matches.models  # noqa: F401

ADMIN_USERNAME = "kuanta"
ADMIN_EMAIL = "dorukhan.erdem@gmail.com"
ADMIN_PASSWORD = "change_me"

def seed_admin(admin_username:str, admin_raw_password:str, admin_email:str | None):
    db = session_local()
    try:
        admin = get_account_by_username(admin_username, db)
        if admin is not None:
            print(f"Admin with {admin_username} already exists")
            return
        admin = AccountModel(
            username = admin_username,
            email = admin_email,
            hashed_password = hash_password(admin_raw_password),
            account_level = settings.ADMIN_ROLE_LEVEL
        )
        db.add(admin)
        db.commit()
        print(f"Admin {admin_username} created.")

    finally:
        db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, default=ADMIN_USERNAME)
    parser.add_argument("--password", type=str, default=ADMIN_PASSWORD)
    parser.add_argument("--email", type=str, default=ADMIN_EMAIL)
    args = parser.parse_args()

    seed_admin(args.username, args.password, args.email)