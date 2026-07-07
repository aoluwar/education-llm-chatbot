"""Redis cache management."""

import json
from typing import Any, Optional

import redis.asyncio as redis

from app.config import settings

_redis_client: Optional[redis.Redis] = None


async def init_redis() -> redis.Redis:
    """Initialize Redis client."""
    global _redis_client
    _redis_client = await redis.from_url(
        settings.REDIS_URL,
        encoding="utf8",
        decode_responses=True,
    )
    return _redis_client


async def get_redis() -> redis.Redis:
    """Get Redis client."""
    if _redis_client is None:
        await init_redis()
    return _redis_client


async def cache_get(key: str) -> Optional[Any]:
    """Get value from cache."""
    redis_client = await get_redis()
    value = await redis_client.get(key)
    if value:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return None


async def cache_set(key: str, value: Any, expire: int = 3600) -> None:
    """Set value in cache."""
    redis_client = await get_redis()
    serialized_value = json.dumps(value) if not isinstance(value, str) else value
    await redis_client.setex(key, expire, serialized_value)


async def cache_delete(key: str) -> None:
    """Delete value from cache."""
    redis_client = await get_redis()
    await redis_client.delete(key)


async def cache_clear_pattern(pattern: str) -> None:
    """Clear cache by pattern."""
    redis_client = await get_redis()
    keys = await redis_client.keys(pattern)
    if keys:
        await redis_client.delete(*keys)
