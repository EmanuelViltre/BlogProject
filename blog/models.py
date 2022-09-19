from unittest.util import _MAX_LENGTH
from django.db import models
import uuid  # importar
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="image")
    body = RichTextField()
    post_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
