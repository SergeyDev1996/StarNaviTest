from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(to=User, related_name="post", on_delete=models.CASCADE)
