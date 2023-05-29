from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(to=User, related_name="post", on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "post")
