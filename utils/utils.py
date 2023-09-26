import json
import time

from config import cache_redis_client as cache_redis


def get_token_from_redis():
    cache_token = cache_redis.get("token")
    if cache_token:
        cache_token = json.loads(cache_token)
        if cache_token["expires_at"] > int(time.time()) + 60:
            return cache_token
    return None
