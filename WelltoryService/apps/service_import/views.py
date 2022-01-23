from django.shortcuts import render
from django.shortcuts import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .celery_tasks import import_task


SERVICE_API_URL = reverse("service_api")


class ImportHandler(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        celery_result = import_task(SERVICE_API_URL, user_id)
        return Response(celery_result)
