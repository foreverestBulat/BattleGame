from typing import Optional
from fastapi import APIRouter, Depends


battle_router = APIRouter(tags=['battle'], prefix='/battle')

@battle_router.get('/{id}')
def get_battle(
        id: int
    ):
    pass

@battle_router.post('/start')
def start_battle():
    pass