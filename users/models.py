from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Mujer'),
        ('female', 'Hombre'),
        ('other', 'Otro')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='users/profile_pictures')
    biography = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=70, blank=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username