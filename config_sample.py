import redis

# cocopilot
COCO_API_URL = "https://api.cocopilot.org"
COCO_TOKEN = "ghu_ThisIsARealFreeCopilotKeyByCoCopilot"

# route
GET_TOKEN_ROUTE = "/copilot_internal/v2/token"

# my_server
my_server = {
    "port": 8080,
    # 用于验证的token，如果不需要验证，则设置为None
    "token": None,
}

# redis
cache_redis_config = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 0,
    "password": None,
    "decode_responses": True,
}
cache_redis_client = redis.Redis(**cache_redis_config)
