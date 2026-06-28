from dataclasses import fields
from core.database import engine, Base
from fastapi import Body, FastAPI
from players.routers import router as player_router
from matches.routers import router as match_router
from auth.routers import router as auth_router
from games.routers import router as game_router



app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(player_router)
app.include_router(match_router)
app.include_router(auth_router)
app.include_router(game_router)

@app.get("/")
async def root():
    return {"message":"Kuantech Game Backend V0.1"}
