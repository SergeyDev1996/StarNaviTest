from django.urls import path, include

urlpatterns = [
    path("", include("api.post.urls")),
    path("user/", include("api.user.urls"))
]
