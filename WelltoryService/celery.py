import os

from celery import Celery


app = Celery("WelltoryService", broker="redis://redis", backend="redis://redis:6379")

app.config_from_object("django.conf.settings", namespace="CELERY")

app.autodiscover_tasks(related_name="celery_tasks")
