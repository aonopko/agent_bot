
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=150)
    telegram_id = models.IntegerField(primary_key=True, unique=True)
