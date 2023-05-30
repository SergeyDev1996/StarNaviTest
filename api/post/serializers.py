from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.post.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id",)


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text", "user", "like_count")
        read_only_fields = ("user", "like_count")


class LikePostSerializer(PostSerializer):

    # def validate(self, attrs):
    #     user = self.context["request"].user
    #     post_id = self.context["view"].kwargs.get("post_id")
    #     try:
    #         post = Post.objects.get(id=post_id)
    #     except Post.DoesNotExist:
    #         raise ValidationError("Post with this id does not exist.")
    #     # Check if the user has already liked the post
    #     if Like.objects.filter(user=user, post=post).exists():
    #         raise serializers.ValidationError("We already have a like from this user.")
    #     return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        post_id = self.context["view"].kwargs.get("post_id")
        like = Like.objects.create(user=user, post_id=post_id)
        return like
