from django.utils import timezone

from api.user.models import CustomUser


class UpdateLastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            CustomUser.objects.filter(id=request.user.id).update(last_request=timezone.now())
        return response
