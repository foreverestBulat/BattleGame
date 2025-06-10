import json
from fastapi import Depends
from redis.asyncio import Redis

from domain.entity import Battle
from persistence.database import get_redis
from dataclasses import asdict


class BattleRepository:
    def __init__(
            self, 
            db: Redis = Depends(get_redis)
        ):
        self.database = db
        
    async def get_by_id_async(self, id: int) -> Battle:
        result = await self.database.get(f'battle:{id}')
        if result:
            return json.loads(result)
        return None
        
    async def create_battle_async(self, battle: Battle, cache_ttl: int = 86400) -> int:
        battle_data = {
            'id': battle.id,
            'fighter_1': asdict(battle.fighter_1),
            'fighter_2': asdict(battle.fighter_2),
            'winner_is_1': battle.winner_is_1
        }
        
        await self.database.set(
            name=f'battle:{battle.id}',
            value=json.dumps(battle_data),
            ex=cache_ttl
        )
        return battle.id