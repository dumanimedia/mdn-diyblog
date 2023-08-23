from django.urls import path
from .views import (
    home_page,
    signup_page,
    posts_page,
    post_details_page,
    create_post_page,
    post_comment_page,
    bloggers_page,
    blogger_details_page,
    become_blogger_page,
)


urlpatterns = [
    path("", home_page, name="home_page"),
    path("accounts/signup/", signup_page, name="signup_page"),
    path("blog/all/", posts_page, name="posts_page"),
    path("blog/new/", create_post_page, name="create_post_page"),
    path("blog/<int:post_id>/", post_details_page, name="post_details_page"),
    path("blog/<int:post_id>/create/", post_comment_page, name="post_comment_page"),
    path("blog/bloggers/", bloggers_page, name="bloggers_page"),
    path(
        "blog/blogger/<int:blogger_id>/",
        blogger_details_page,
        name="blogger_details_page",
    ),
    path("blog/bloggers/new/", become_blogger_page, name="become_blogger_page"),
]
