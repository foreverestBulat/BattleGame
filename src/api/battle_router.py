from typing import Optional
from fastapi import APIRouter, Depends

from application.battle_service import BattleService
from application.models_and_dto import CreateBattleRequest


battle_router = APIRouter(tags=['battle'], prefix='/battle')

@battle_router.get('/{id}')
async def get_battle(
        id: int,
        service: BattleService = Depends()
    ):
    return await service.get_result_battle_async(id=id)
    

@battle_router.post('/start')
async def start_battle(
        request: CreateBattleRequest,
        service: BattleService = Depends()
    ):
    return await service.create_and_start_battle_async(request=request)