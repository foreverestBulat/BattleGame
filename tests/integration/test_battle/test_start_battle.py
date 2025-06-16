import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_start_battle_success(client: TestClient):
    request_data = {
        'fighter_1': {'name': 'Воин', 'power': 60},
        'fighter_2': {'name': 'Рыцарь', 'power': 50}
    }
    
    response = client.post("/battle/start", json=request_data)
    
    assert response.status_code == 200
    json = response.json()
    assert isinstance(json, int)
    assert json == 1


@pytest.mark.asyncio
async def test_start_battle_invalid_input(client: TestClient):
    request_data = {
        'fighter_1': {
            'name': 'Воин',
            'power': 60
        }
        # нет fighter_2
    }
    
    response = client.post('/battle/start', json=request_data)
    
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY