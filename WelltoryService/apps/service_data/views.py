import requests
from django.urls import reverse

from .serializers import WeightSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .celery_tasks import data_process_task
from .models import UserWeight
from WelltoryService.apps.service_import.celery_tasks import import_task


class ImportApiView(APIView):
    serializer_class = WeightSerializer

    def get(self, request):
        service_import_url = reverse("service_import:import")
        service_api_url = reverse("service_api:list")
        url = f"http://host.docker.internal:8000{service_import_url}"
        redis_key = requests.get(url).text
        import_task.apply_async(
            args=[service_api_url, redis_key], link=data_process_task.s()
        )
        return Response(status=201)


class ServiceDataApiView(generics.RetrieveAPIView):
    queryset = UserWeight.objects.all()
    serializer_class = WeightSerializer
