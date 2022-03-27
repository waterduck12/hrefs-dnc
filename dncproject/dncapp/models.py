from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} / {self.author}'

class Post(models.Model):
    day = models.DateField(auto_now=True)
    cookname = models.TextField(default='')

    def __str__(self):
        return self.day

    def __str__(self):
        return self.cookname