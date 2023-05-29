from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.post.models import Post, Like
from api.post.serializers import PostCreateSerializer


class CreatePostView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(APIView):
    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()  # User wants to unlike the post
            return Response({'message': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            Like.objects.create(user=user, post=post)
            return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)
