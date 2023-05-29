from rest_framework import serializers

from api.post.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("text", "user")
        read_only_fields = ("user",)
