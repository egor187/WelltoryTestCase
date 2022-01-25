from django.shortcuts import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .celery_tasks import import_task
from uuid import uuid4
from celery.utils.log import get_task_logger
from celery.exceptions import SoftTimeLimitExceeded

logger = get_task_logger(__name__)


class ImportHandler(APIView):
    def post(self, request):
        redis_key = str(uuid4())
        user_id = request.data.get("user_id")
        service_api_url = reverse("service_api:detail", args=[user_id])
        try:
            task_result = import_task.delay(service_api_url, redis_key)
        except SoftTimeLimitExceeded as e:
            logger.info(f"Task exc time is exceeded: {e}")
            return Response(e)
        else:
            return Response(task_result.get())
