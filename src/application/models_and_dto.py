from pydantic import BaseModel

class CreateFighterRequest(BaseModel):
    name: str
    power: int

class CreateBattleRequest(BaseModel):
    fighter_1: CreateFighterRequest
    fighter_2: CreateFighterRequest

class GetBattleResultDto(BaseModel):
    winner: str
    
    @staticmethod
    def create(name: str):
        return GetBattleResultDto(winner=name)