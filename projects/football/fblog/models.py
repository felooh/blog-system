from django.db import models
from django.contrib.auth.models import User
from django.db import models

# class Author(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
   ## profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    post_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

