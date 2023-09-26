import json

import requests
from flask import Flask, jsonify, request

from config import COCO_API_URL, COCO_TOKEN, GET_TOKEN_ROUTE
from config import cache_redis_client as cache_redis
from config import my_server
from utils.utils import get_token_from_redis

app = Flask(__name__)


def require_token(fun):
    def wrapper(*args, **kwargs):
        if (
            my_server["token"]
            and request.headers.get("Authorization", "")
            != "token " + my_server["token"]
        ):
            return jsonify({"message": "token is invalid"}), 401
        return fun(*args, **kwargs)

    return wrapper


@app.route(GET_TOKEN_ROUTE, methods=["GET"])
@require_token
def get_token():
    token = get_token_from_redis()
    if not token:
        headers = {"Authorization": "token " + COCO_TOKEN}
        response = requests.get(COCO_API_URL + GET_TOKEN_ROUTE, headers=headers)
        if response.status_code == 200:
            token = response.json()
            cache_redis.set("token", json.dumps(token))
        else:
            return response.json, response.status_code
    return jsonify(token)


if __name__ == "__main__":
    app.run(host=my_server["host"], port=my_server["port"])
