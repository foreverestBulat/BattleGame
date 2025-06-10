from fastapi import FastAPI

from api.battle_router import battle_router


app = FastAPI()

app.include_router(battle_router)