import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

import sys
from pathlib import Path
from redis.asyncio import Redis

sys.path.append(str(Path(__file__).parent.parent.parent / 'src'))
from main import app
from persistence.database import get_redis


@pytest.fixture
def mock_redis():
    redis_mock = AsyncMock(spec=Redis)
    redis_mock.get = AsyncMock()
    redis_mock.set = AsyncMock()
    return redis_mock

@pytest.fixture
def client(mock_redis):
    async def override_redis():
        return mock_redis
    app.dependency_overrides[get_redis] = override_redis
    return TestClient(app)