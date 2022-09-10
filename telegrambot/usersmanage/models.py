from django.db import models


class Manager(models.Model):
    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджера"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name="ID Менеджера у Телеграмі")
    name = models.CharField(max_length=100, verbose_name="Ім'я менеджера")
    user_name = models.CharField(max_length=155, verbose_name="Username Телеграм")

