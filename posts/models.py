"""Posts models"""

from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from datetime import datetime

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='posts/photos')
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_date(self):
        time = datetime.now()
        if self.created.day == time.day:
            return "hace " + str(time.hour - self.created.hour) + " horas"
        else:
            if self.created.month == time.month:
                return "hace " + str(time.day - self.created.day) + " días"
            else:
                if self.created.year == time.year:
                    return "hace " + str(time.month - self.created.month) + " meses"
        return self.created

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now=True)

    def get_date(self):
        time = datetime.now()
        if self.created.day == time.day:
            return str(time.hour - self.created.hour) + " h"
        else:
            if self.created.month == time.month:
                return str(time.day - self.created.day) + " d"
            else:
                if self.created.year == time.year:
                    return str(time.month - self.created.month) + " m"
        return self.created

    def __str__(self):
        return self.text


class SavedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    