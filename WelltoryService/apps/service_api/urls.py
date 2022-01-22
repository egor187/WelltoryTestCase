from django.urls import path
from . import views

urlpatterns = [
    path('external-fake-api/', views.WeightList.as_view()),
    path('external-fake-api/<int:pk>/', views.WeightDetail.as_view()),
]