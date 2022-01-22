from rest_framework import serializers
from .models import Weight


class WeightSerializer(serializers.ModelSerializer):
    unit = serializers.ReadOnlyField(source="unit.unit")
    id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Weight
        fields = ["id", "weight", "unit", "date"]
