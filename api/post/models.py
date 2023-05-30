from django.conf import settings
from django.db import models

from api.user.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name="post", on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)

    @property
    def like_count(self):
        return Like.objects.filter(post=self).count()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # class Meta:
    #     unique_together = ("user", "post")
