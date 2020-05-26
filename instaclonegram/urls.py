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
    path('', include(('posts.urls', 'posts'), namespace='posts')),

    
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/update-profile/', users_views.update_profile, name='update-profile'),
    path('users/profile/', users_views.profile, name='profile'),
    #path('posts/',  posts_views.posts, name='home'),
    #path('posts/new-post/', posts_views.new_post, name='new-post'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
