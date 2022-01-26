from django.urls import path
from .views import ImportApiView, ServiceDataApiView


app_name = "service_data"

urlpatterns = [
    path("", ImportApiView.as_view()),
    path("<int:pk>/", ServiceDataApiView.as_view()),
]
