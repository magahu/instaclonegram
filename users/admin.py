from django.contrib import admin
from users.models import Profile
from users.models import Follow

admin.site.register(Profile)
admin.site.register(Follow)