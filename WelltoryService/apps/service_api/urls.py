from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeightList.as_view()),
    path('<int:pk>/', views.WeightDetail.as_view()),
]