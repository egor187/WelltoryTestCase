from django.db import models


class UserWeight(models.Model):
    weight = models.FloatField()
    day = models.DateField(auto_now=True)
    user_id = models.IntegerField()

    def __str__(self):
        return f"{self.user_id}: {self.weight}"
