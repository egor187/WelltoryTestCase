from django.urls import path
from . import views


app_name = "service_api"
# external-fake-api/
urlpatterns = [
    path("", views.WeightList.as_view(), name="list"),
    path("<int:pk>/", views.WeightDetail.as_view(), name="detail"),
]
