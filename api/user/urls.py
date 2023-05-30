from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.user.views import UserSignUpView, UserActivityView

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="sign_up"),
    path("activity/", UserActivityView.as_view(), name="user-activity"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
