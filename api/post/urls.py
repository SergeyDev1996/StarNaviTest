from django.urls import path

from api.post.views import (CreatePostView,
                            LikePostView,
                            UnlikePostView,
                            AnalyticsView)


urlpatterns = [
    path("create/", CreatePostView.as_view(),
         name="create_post"),
    path("<int:post_id>/like/", LikePostView.as_view(),
         name="like-post"),
    path("<int:post_id>/unlike/", UnlikePostView.as_view(),
         name="unlike-post"),
    path("analytics/", AnalyticsView.as_view(),
         name="analytics"),
]
