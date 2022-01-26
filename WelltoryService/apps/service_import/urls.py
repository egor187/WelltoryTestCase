from django.urls import path
from .views import ImportHandler


app_name = 'service_import'

urlpatterns = [
    path('', ImportHandler.as_view(), name="import"),
]