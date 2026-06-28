from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    # check_same_thread sadece SQLite'a özgü (tek dosya, thread kısıtı)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    # PostgreSQL gibi gerçek DB sunucuları için connection pooling
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_size=10,        # havuzda sürekli açık tutulan bağlantı sayısı
        max_overflow=20,     # ani yükte açılabilecek geçici ekstra bağlantı
        pool_pre_ping=True,  # kullanmadan önce bağlantı canlı mı diye kontrol
    )

session_local = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

DbSession = Annotated[Session, Depends(get_db)]
