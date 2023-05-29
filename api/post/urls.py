from django.urls import path

from api.post.views import CreatePostView

urlpatterns = [
    path("create-post", CreatePostView.as_view(), name="create_post")
]
