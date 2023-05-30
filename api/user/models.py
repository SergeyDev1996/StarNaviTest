from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_request = models.DateTimeField(auto_now_add=True, null=True)
