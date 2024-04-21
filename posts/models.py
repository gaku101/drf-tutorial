from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField(max_length=2000)
  published = models.BooleanField(default=False)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_user')

  def __str__(self):
    return self.title
