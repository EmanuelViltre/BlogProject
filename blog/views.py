from django.shortcuts import render
from turtle import pos
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {"post": post, "posts": posts}
    return render(request, "blog/detail.html", context)


@login_required
def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            messages.info(request, "Article created succesfully")
            return redirect("index")
        else:
            messages.error(request, "Article not created")
    context = {"form": form}
    return render(request, "blog/create.html", context)


@login_required
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, "Article Updated")
            return redirect("detail", slug=post.slug)
    context = {"form": form}
    return render(request, "blog/create.html", context)


@login_required
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == "POST":
        post.delete()
        messages.info(request, "Article Deleted")
        return redirect("index")
    context = {"form": form}
    return render(request, "blog/delete.html", context)


def about(request):
    return render(request, "blog/about.html")
