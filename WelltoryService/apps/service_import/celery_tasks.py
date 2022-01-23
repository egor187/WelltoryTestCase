from celery import shared_task
from WelltoryService.redis_client import redis_cli

import requests


@shared_task
def import_task(url, user_id):
    api_url = url + user_id
    user_data = requests.post(api_url).json()
    redis_key = f"user_id_redis_key_{str(user_id)}"
    redis_cli.set(redis_key, user_data)
    return redis_key
