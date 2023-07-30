from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Timelog(models.Model):
    image = models.ImageField(verbose_name="image")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="image")
