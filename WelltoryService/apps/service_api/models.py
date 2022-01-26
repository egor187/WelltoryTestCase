from django.db import models
from django.contrib.auth import get_user_model


class WeightUnit(models.Model):
    unit = models.TextField()

    def __str__(self):
        return self.unit


class Weight(models.Model):
    weight = models.FloatField()
    date = models.DateField(auto_now=True)
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="weight"
    )
    unit = models.ForeignKey(WeightUnit, on_delete=models.PROTECT, related_name="+")

    def __str__(self):
        return f"{self.user}: {self.weight} {self.unit}"
