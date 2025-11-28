from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path("<int:post_id>/", views.single_post, name="single-post"),
]
