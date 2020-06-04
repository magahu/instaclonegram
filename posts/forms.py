"""Posts forms"""

from django import forms
from posts.models import Post, Like

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'picture', 'description')

class LikeForm(forms.ModelForm):
        model = Like
        fields = ('user', 'post', 'n_likes')

    