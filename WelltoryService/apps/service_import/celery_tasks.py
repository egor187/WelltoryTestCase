import requests

from WelltoryService.redis_client import redis_cli_prod
from WelltoryService.celery import app
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task
def import_task(service_api_url,  redis_key):
    try:
        url = f"http://host.docker.internal:8000{service_api_url}"
        user_data = requests.get(url).text
        redis_cli_prod.set(redis_key, user_data)
        return redis_key
    except SoftTimeLimitExceeded:
        raise
