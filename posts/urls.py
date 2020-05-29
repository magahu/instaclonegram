"""Posts URL Configuration"""

from django.urls import path
from posts import views

urlpatterns = [

     path('feed/',  views.posts, name='home'),
     path('new-post/', views.new_post, name='new-post'),

]

