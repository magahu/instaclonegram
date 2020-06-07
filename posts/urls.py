"""Posts URL Configuration"""

from django.urls import path
from posts import views

urlpatterns = [

     path('feed/',  views.posts, name='home'),
     path('new-post/', views.new_post, name='new-post'),
     path('like/', views.new_like, name='like'),
     path('new-comment/', views.new_comment, name='new-comment'),
     path('<int:pk>/comments/', views.list_comments, name='show-comments')

]


