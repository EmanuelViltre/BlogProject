from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", login_request, name="login"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path(
        "logout/",
        LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    path("editProfile/", editProfile, name="editProfile"),
    path("uploadAvatar/", uploadAvatar, name="uploadAvatar"),
]
