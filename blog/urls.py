from django.urls import path
from .views import (
    get_posts,
    get_users,
    summarize_post_view,
    generate_post_view,
)

urlpatterns = [
    path('posts/manual/', get_posts),
    path('users/', get_users),
    path('posts/summarize/', summarize_post_view),
    path('posts/generate/', generate_post_view),
]