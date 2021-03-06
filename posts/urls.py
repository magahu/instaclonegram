"""Posts URL Configuration"""

from django.urls import path
from posts import views

urlpatterns = [

     path('home/',  views.HomePostsList.as_view(), name='home'),
     #path('new-post/', views.new_post, name='new-post'),
     path('new-post/', views.CreatePostView.as_view(), name='new-post'),
     path('like/', views.new_like, name='like'),
     path('<int:pk>/new-comment/', views.new_comment, name='new-comment'),
     #path('<int:pk>/comments/', views.list_comments, name='show-comments'),
     path('<int:pk>/comments/', views.PostDetail.as_view(), name='show-comments'),
     #path('<int:pk>/<int:comment_pk>/comments/', views.list_comments, name='show-comments-reply'),
     path('<int:pk>/<int:comment_pk>/comments/', views.PostDetail.as_view(), name='show-comments-reply'),
     path('<int:pk>/likes/', views.list_likes, name='show-likes'),
     path('saved_posts/', views.list_saved_posts, name='show-saved'),
     path('save_post/', views.save_post, name='save'),
     path('<int:post_pk>/delete/', views.delete_post, name='delete'),
     path('<int:comment_pk>/like/', views.like_comment, name='comment-like'),
     path('<int:comment_pk>/reply/', views.new_reply, name='reply'),
     path('<int:comment_pk>/create-reply', views.create_reply, name='create-reply'),
     path('<int:reply_pk>/reply-like/', views.like_reply, name='reply-like')
     
]


