from fastapi import APIRouter, Query, status, HTTPException

router = APIRouter(
    prefix="/players",
    tags=["Player"] # What is this?
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_players(sort_by: str = Query(default="rank")):
    return {"players":""}

@router.get("/lookup/{username}")
async def lookup_player(username: str):
    return {"player":{"username":username}}