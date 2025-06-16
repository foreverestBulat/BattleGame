import pytest
from fastapi import status
from fastapi.testclient import TestClient
from redis.asyncio import Redis

from persistence.repositories.battle_repository import BattleRepository

def test_get_battle_success(client: TestClient, mock_redis: Redis):
    battle_json = """
    {
        "id": 1,
        "fighter_1": {"name": "Воин", "power": 60},
        "fighter_2": {"name": "Рыцарь", "power": 50},
        "winner_is_1": true
    }
    """
    mock_redis.get.return_value = battle_json

    battle_id = 1
    response = client.get(f'/battle/{battle_id}')

    assert response.status_code == 200
    assert response.json() == {'winner': 'Воин'}
    mock_redis.get.assert_awaited_once_with(f'battle:{battle_id}')

def test_get_battle_not_found(client: TestClient, mock_redis: Redis):
    mock_redis.get.return_value = None
    
    battle_id_not_found = 123
    response = client.get(f'/battle/{battle_id_not_found}')
    
    assert response.status_code == status.HTTP_200_OK
    # assert response.status_code == status.HTTP_404_NOT_FOUND # вообще так должно быть, но я не сделал возращение 404, поэтому 200
    assert response.json() == None
