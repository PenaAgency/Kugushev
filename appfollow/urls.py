from django.contrib import admin
from django.urls import path
from core.views import HackerNewsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', HackerNewsList.as_view())
]
