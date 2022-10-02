
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150)
    telegram_id = models.IntegerField()
