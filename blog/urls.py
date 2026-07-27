from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    hello,
    get_posts,
    get_users,
    summarize_post_view,
    generate_post_view,
    PostViewSet,
)

router = DefaultRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('hello/', hello),
    path('posts/manual/', get_posts),
    path('users/', get_users),
    path('posts/summarize/', summarize_post_view),
    path('posts/generate/', generate_post_view),
]

urlpatterns += router.urls