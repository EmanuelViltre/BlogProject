from django.shortcuts import render
from .forms import UserRegisterForm, UserEditForm, AvatarForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Avatar


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Created User")
            return render(
                request,
                "blog/index.html",
            )
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = request.POST["username"]
            password = request.POST["password"]

            usuario = authenticate(username=user, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.info(request, "Bienvenido")
                return render(
                    request,
                    "blog/index.html",
                )
            else:
                messages.info(request, "Incorrect User or Password")
                return render(
                    request,
                    "user/login.html",
                )
        else:
            messages.info(request, "Incorrect User or Password")
            return render(
                request,
                "user/login.html",
            )
    else:
        form = AuthenticationForm()
        return render(request, "user/login.html", {"form": form})


@login_required
def editProfile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.save()
            messages.info(request, "Edited Profile")
            return render(
                request,
                "blog/index.html",
            )
    else:
        form = UserEditForm(instance=user)
    return render(request, "user/editProfile", {"form": form})


@login_required
def profile(request):
    return render(request, "user/profile.html")


def uploadAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            oldAvatar = Avatar.objects.filter(user=request.user)
            if len(oldAvatar) > 0:
                oldAvatar.delete()
            avatar = Avatar(user=request.user, image=form.cleaned_data["image"])
            avatar.save()
            return render(
                request,
                "blog/index.html",
                {
                    "user": request.user,
                    "menssage": "Avatar Changed",
                    "image": obteinAvatar(request),
                },
            )
    else:
        form = AvatarForm()
    return render(
        request,
        "user/uploadAvatar.html",
        {"form": form, "user": request.user, "image": obteinAvatar(request)},
    )


def obteinAvatar(request):
    list = Avatar.objects.filter(user=request.user)
    if len(list) != 0:
        image = list[0].image.url
    else:
        image = ""
    return image
