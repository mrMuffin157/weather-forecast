from django.db import models

# Create your models here.

class weather(models.Model):
    temperature = models.FloatField()
    location = models.CharField(max_length=25)
