from fastapi import Depends
from application.models_and_dto import CreateBattleRequest, GetBattleResultDto
from config import ADD_MAX_POWER_RANDOM, ADD_MIN_POWER_RANDOM
from domain.entity import Battle, Fighter
from persistence.repositories.battle_repository import BattleRepository
from random import randint


class BattleService:
    def __init__(
            self,
            repo: BattleRepository = Depends()
        ):
        self.reposioty = repo
    
    async def get_result_battle_async(self, id: int):
        result = await self.reposioty.get_by_id_async(id=id)
        if result:
            return GetBattleResultDto.create(name=result['fighter_1']['name'] if result['winner_is_1'] else result['fighter_2']['name'])
        return None
    
    async def create_and_start_battle_async(self, request: CreateBattleRequest):
        battle = Battle(
            fighter_1=Fighter(name=request.fighter_1.name, power=request.fighter_1.power),
            fighter_2=Fighter(name=request.fighter_2.name, power=request.fighter_2.power),
            winner_is_1=request.fighter_1.power + randint(ADD_MIN_POWER_RANDOM, ADD_MAX_POWER_RANDOM) > request.fighter_2.power + randint(ADD_MIN_POWER_RANDOM, ADD_MAX_POWER_RANDOM)
        )
        
        await self.reposioty.create_battle_async(
            battle=battle
        )
        return battle.id
        