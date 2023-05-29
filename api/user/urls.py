from django.urls import path

from api.user.views import UserSignUpView

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="sign_up")
]
