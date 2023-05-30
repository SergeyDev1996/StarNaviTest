from django.db.models import Count
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.post.models import Like
from api.post.serializers import PostCreateSerializer, LikePostSerializer
from api.user.permissions import IsAuthenticatedAndLastRequest


class CreatePostView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndLastRequest,)
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndLastRequest,)
    serializer_class = LikePostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UnlikePostView(DestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndLastRequest,)
    queryset = Like.objects.all()

    def get_object(self):
        try:
            like = Like.objects.get(
                user=self.request.user, post_id=self.kwargs["post_id"]
            )
        except Like.DoesNotExist:
            raise ValidationError("We do not have any likes from this user.")
        return like


class AnalyticsView(APIView):
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
