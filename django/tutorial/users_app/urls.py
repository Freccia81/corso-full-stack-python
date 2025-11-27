from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list-users"),
    path('create/', views.create_user, name="create-user"),
    path('update/', views.update_user, name="update-user"),
]
