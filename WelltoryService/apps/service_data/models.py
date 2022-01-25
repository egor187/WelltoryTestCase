from django.db import models
from django.contrib.auth import get_user_model


class UserWeight(models.Model):
    weight = models.FloatField()
    date = models.DateField(auto_now=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="weight")

    def __str__(self):
        return f"{self.user}: {self.weight}"
