from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contattaci/", views.contact, name="contact"),
    path("posts/", views.posts, name="posts"),
    path('users/create/', views.create_user, name="create-user"),
    path('users/update/', views.update_user, name="update-user")
]