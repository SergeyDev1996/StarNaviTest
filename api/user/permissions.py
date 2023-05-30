from django.conf import settings
from django.utils import timezone
from rest_framework.permissions import BasePermission

from api.post.models import Post
from api.user.models import CustomUser


class IsAuthenticatedAndLastRequest(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

