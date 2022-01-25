from django.urls import path
from . import views


app_name = 'service_api'

urlpatterns = [
    path('', views.WeightList.as_view()),
    path('<int:pk>/', views.WeightDetail.as_view(), name="detail"),
]