from fastapi import APIRouter, Depends, Query, status, HTTPException
from core.database import DbSession, get_db
import matches.services
from matches.schemas import MatchData
from matches.dependencies import verify_service_key

router = APIRouter(
    prefix="/match",
    tags=["Match"]
)

@router.get("/", response_model=list[MatchData], status_code=status.HTTP_200_OK)
async def get_all_matches(db: DbSession):
    return matches.services.get_all_matches(db)

@router.get("/lookup/{match_id}", response_model=MatchData, status_code=status.HTTP_200_OK)
async def lookup_match(match_id: int, db: DbSession):
    single_match = matches.services.get_match_by_id(db, match_id)
    if single_match is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    return single_match

@router.post(
    "/create",
    response_model=MatchData,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_service_key)],
)
async def create_match(match_data: MatchData, db: DbSession):
    new_match = matches.services.create_match(db, match_data)
    return new_match