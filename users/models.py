"""Users models"""

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='users/profile_pictures')
    biography = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=70)
    phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
      follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_follows')
      followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_is_followed')
      created = models.DateTimeField(auto_now=True)

      def __str__(self):
          return self.follower.username+", "+self.followed.username