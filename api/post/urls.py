from django.urls import path

from api.post.views import CreatePostView, LikePostView

urlpatterns = [
    path("create/", CreatePostView.as_view(), name="create_post"),
    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
]
