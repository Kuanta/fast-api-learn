from fastapi import APIRouter, Depends, Query, status, HTTPException
from core.database import DbSession, get_db
import matches.services


router = APIRouter(
    prefix="/match",
    tags=["Match"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_matches(db: DbSession):
    all_matches = matches.services.get_all_matches(db)
    return {"matches":all_matches}

@router.get("/lookup/{match_id}")
async def lookup_match(match_id: int, db: DbSession):
    single_match = matches.services.get_match_by_id(db, match_id)
    #todo: Check if match found
    return {"match":single_match}
