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
        elif self.created.month == time.month:
            return "hace " + str(time.day - self.created.day) + " días"
        elif self.created.year == time.year:
            return "hace " + str(time.month - self.created.month) + " meses"
        return self.created

    def __str__(self):
        return self.title


class LikeInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_date(self):
        time = datetime.now()
       
        if self.created.day == time.day:
            return str(time.hour - self.created.hour) + " h"
        elif self.created.month == time.month:
            return str(time.day - self.created.day) + " d"
        elif self.created.year == time.year:
            return str(time.month - self.created.month) + " m"
        return self.created


class Like(LikeInfo):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title


class SavedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class CommentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_date(self):
        time = datetime.now()
        if self.created.day == time.day:
            return str(time.hour - self.created.hour) + " h"
        elif self.created.month == time.month:
            return str(time.day - self.created.day) + " d"
        elif self.created.year == time.year:
            return str(time.month - self.created.month) + " m"
        return self.created


class Comment(CommentInfo):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class CommentLike(LikeInfo):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment.text


class Reply(CommentInfo):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class ReplyLike(LikeInfo):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply.text
    
    
