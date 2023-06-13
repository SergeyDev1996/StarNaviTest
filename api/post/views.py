from django.db.models import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from post.models import Like, Post
from api.post.serializers import PostCreateSerializer, LikePostSerializer


class CreatePostView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LikePostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)


class UnlikePostView(DestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()

    def get_object(self):
        try:
            like = Like.objects.get(
                user=self.request.user, post_id=self.kwargs["post_id"]
            )
        except Like.DoesNotExist:
            raise ValidationError("We do not have any likes from"
                                  " this user for this post.")
        return like


class AnalyticsView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        # Set default date range if not provided
        if not date_from:
            date_from = timezone.now().date()
        if not date_to:
            date_to = timezone.now().date()
        # Query the database to get analytics data

        analytics = (
            Like.objects.filter(created_at__date__range=[date_from, date_to])
            .values("created_at__date")
            .annotate(likes_count=Count("id"))
            .order_by("created_at__date")
        )
        # Prepare the response data
        response_data = []
        for entry in analytics:
            response_data.append(
                {
                    "date": entry["created_at__date"],
                    "likes_count": entry["likes_count"],
                }
            )
        return Response(response_data)
