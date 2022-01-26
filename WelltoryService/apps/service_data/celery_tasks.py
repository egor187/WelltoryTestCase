import json

from WelltoryService.redis_client import redis_cli_prod
from WelltoryService.celery import app
from celery.utils.log import get_task_logger
from redis.exceptions import DataError
from .serializers import WeightSerializer


logger = get_task_logger(__name__)


@app.task
def data_process_task(redis_key):
    try:
        users_data = json.loads(redis_cli_prod.get(redis_key).decode("utf-8"))
        odd = [obj for obj in users_data if int(obj["weight"]) % 2 == 0]
        for obj in odd:
            serializer = WeightSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
    except DataError as e:
        logger.info(e)
        raise
