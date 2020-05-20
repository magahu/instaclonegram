"""instaclonegram URL Configuration"""

from django.contrib import admin
from django.urls import path
from users import views as users_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', users_views.login_view, name='login'),
    path('users/login/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('posts/',  posts_views.posts, name='home'),
]
