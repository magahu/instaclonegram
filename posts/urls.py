"""Posts URL Configuration"""

from django.urls import path
from posts import views

urlpatterns = [

     path('feed/',  views.home, name='home'),
     path('new-post/', views.new_post, name='new-post'),
     path('like/', views.new_like, name='like'),
     path('<int:pk>/new-comment/', views.new_comment, name='new-comment'),
     path('<int:pk>/comments/', views.list_comments, name='show-comments'),
     path('<int:pk>/likes/', views.list_likes, name='show-likes'),
     path('saved_posts/', views.list_saved_posts, name='show-saved'),
     path('save_post/', views.save_post, name='save'),
     path('<int:post_pk>/delete/', views.delete_post, name='delete')
     
  

]


