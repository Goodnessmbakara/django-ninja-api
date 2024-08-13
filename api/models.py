from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=400)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
