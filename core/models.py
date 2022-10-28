from django.db import models


class HackerNews(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
