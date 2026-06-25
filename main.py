from dataclasses import fields

from fastapi import Body, FastAPI
from players.routers import router as player_router


app = FastAPI()

app.include_router(player_router)

@app.get("/")
async def root():
    return {"message":"Kuantech Game Backend V0.1"}

#from models.player import Player, PlayerInputData, PlayerUpdateData
# players = [Player("Kuanta", 10), Player("Hellion", 200), Player("Shadow",300)]

# @app.get("/")
# def home():
#     return {"message": "Selam Dorukhan, FastAPI uykudan uyandı!"}

# @app.get("/players")
# async def get_players(sort_by: str = "rank"):
#     return players

# @app.post("/players/create_player")
# async def create_player(new_player_body: PlayerInputData):

#     # Parse
#     new_player = Player(**new_player_body.model_dump())
#     players.append(new_player)
#     return {"message":f"{new_player.username} inserted"}


# @app.get("/player/{username}")
# async def get_player(username:str):
#     for player in players:
#         if username.lower() == player.username.lower():
#             return {"player":player}
#     return {"player":""}

# @app.put("/players/update")
# async def update_player(update_fields:PlayerUpdateData):
#     for player in players:
#         if player.username.lower() == update_fields.username.lower():
#             update_dict = update_fields.model_dump(exclude_none=True)
#             for key, value in update_dict.items():
#                 setattr(player, key, value)
#             return {f"{player.username} has been updated"}
#     return {"No user found"}

# @app.delete("/players/delete/{username}")
# async def delete_player(username:str):
#     index_to_pop = -1
#     for i in range(len(players)):
#         if players[i].username.lower() == username.lower():
#             index_to_pop = i
#             break
#     if index_to_pop < 0:
#         return {"message":"Player not found"}
    
#     player_to_delete = players[index_to_pop]
#     players.pop(index_to_pop)
#     return {"message":f"{player_to_delete.username} has been deleted"}