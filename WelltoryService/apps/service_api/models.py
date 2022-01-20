from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class WelltoryUser(AbstractUser):

    weight = models.FloatField()

    def __str__(self):
        return self.get_full_name()


class WeightUnit(models.Model):
    unit = models.TextField()

    def __str__(self):
        return self.unit
