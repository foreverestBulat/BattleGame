import datetime
import itertools
from typing import List, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class Fighter:
    name: str = None
    power: int = None
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Battle:
    _next_id: int = 1
    id: int = field(default=None, init=False)
    fighter_1: Fighter = None
    fighter_2: Fighter = None
    winner_is_1: bool = None
    
    def __post_init__(self):
        if self.id is None:
            self.id = Battle._next_id
            Battle._next_id += 1
            
            
    def to_dict(self):
        return {
            'id': self.id,
            'fighter_1': self.fighter_1.to_dict(),
            'fighter_2': self.fighter_2.to_dict(),
            'winner_is_1': self.winner_is_1
        }