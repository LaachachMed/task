from django.db import models


# Create your models here.

# our Model
class task_data(models.Model):
    timestamp = models.CharField(max_length=256)
    temperature = models.FloatField()
    duration = models.CharField(max_length=256)