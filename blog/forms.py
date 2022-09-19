from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["slug"]
