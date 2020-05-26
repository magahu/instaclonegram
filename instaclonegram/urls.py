"""instaclonegram URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from posts import views as posts_views
#access to images
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
