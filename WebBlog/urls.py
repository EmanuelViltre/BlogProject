from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from blog.views import *

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("user/", include("user.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
