from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.WeightList.as_view()),
    path('users/<int:pk>/', views.WeightDetail.as_view()),
]