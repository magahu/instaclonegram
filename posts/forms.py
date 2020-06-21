"""Posts forms"""

from django import forms
from posts.models import Post, Like, Comment, SavedPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'picture', 'description')


class NewLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('post', 'user')


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')

class SavedPostForm(forms.ModelForm):
    class Meta:
        model = SavedPost
        fields = ('post', 'user')
    

    