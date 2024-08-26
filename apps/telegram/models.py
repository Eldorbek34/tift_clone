from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)