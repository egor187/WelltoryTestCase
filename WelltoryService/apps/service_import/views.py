from django.shortcuts import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .celery_tasks import import_task
from uuid import uuid4
from celery.exceptions import SoftTimeLimitExceeded
from loguru import logger


class ImportHandler(APIView):
    def get(self, request):
        redis_key = str(uuid4())
        service_api_url = reverse("service_api:list")
        try:
            task_result = import_task.delay(service_api_url, redis_key).get()
        except SoftTimeLimitExceeded as e:
            logger.info(f"Task exc time is exceeded: {e}")
            return Response(e)
        else:
            return Response(task_result)
