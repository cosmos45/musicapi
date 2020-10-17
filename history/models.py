from django.db import models
from django.contrib.auth.models import User


class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=100000000, default="")