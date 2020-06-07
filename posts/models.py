"""Posts models"""

from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='posts/photos')
    description = models.TextField(max_length=500, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.liked_post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


    
    