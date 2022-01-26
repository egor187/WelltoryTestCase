from rest_framework import serializers
from .models import UserWeight


class WeightSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="user_id")
    date = serializers.DateField(source="day")

    class Meta:
        model = UserWeight
        fields = ["id", "weight", "date"]
