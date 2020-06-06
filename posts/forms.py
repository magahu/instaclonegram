"""Posts forms"""

from django import forms
from posts.models import Post, Like, Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'picture', 'description')


class NewLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('liked_post', 'user')


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commented_post', 'user', 'comment')
    

    