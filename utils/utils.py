import json
import time

from config import cache_redis_client as cache_redis

TOKEN_CACHE_KEY = "token"
TOKEN_EXPIRATION_TIME = 60

def get_token_from_redis():
    try:
        cache_token = cache_redis.get(TOKEN_CACHE_KEY)
        if cache_token:
            cache_token = json.loads(cache_token)
            if cache_token["expires_at"] > int(time.time()) + TOKEN_EXPIRATION_TIME:
                return cache_token
    except Exception as e:
        print(f"ERROR: get token from redis failed, {e=}")
        pass
    return None