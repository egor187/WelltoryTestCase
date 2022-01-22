from .serializers import WeightSerializer
from .models import Weight
from rest_framework import generics


class WeightList(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class WeightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
