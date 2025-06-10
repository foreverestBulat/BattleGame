from redis.asyncio import Redis
from redis.asyncio.connection import ConnectionPool
from config import REDIS_URL


redis_pool = ConnectionPool.from_url(REDIS_URL)

async def get_redis() -> Redis:
    redis = Redis(connection_pool=redis_pool)
    try:
        yield redis
    finally:
        await redis.close()