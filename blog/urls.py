from operator import index
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("article/<str:slug>", detail, name="detail"),
    path("create", createPost, name="create"),
    path("update-post/<str:slug>", updatePost, name="updatepost"),
    path("delete-post/<str:slug>", deletePost, name="deletepost"),
    path("about", about, name="about"),
]
