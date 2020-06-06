"""Posts views Configuration"""

from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewLikeForm, NewCommentForm
from posts.models import Post, Like, Comment


#Create new post view
@login_required
def new_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        # create a form instance and populate it with data from the request:
        form = NewPostForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid(): 
            form.save()
            # redirect to a new URL:
            return redirect('posts:home')
    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewPostForm()
    return render(request, 'posts/new_post.html', {'form':form})


#Home view
@login_required
def posts(request):
    posts = Post.objects.all().order_by('-posted')
    return render(request, 'home.html', {'posts':posts})


#Like view
@login_required
def new_like(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewLikeForm(request.POST)
       
        liked_post = request.POST['liked_post']
        user = request.POST['user']
        like = Like.objects.filter(liked_post=liked_post, user=user)
        #import pdb; pdb.set_trace()
        # check whether it's valid:
        if like:
            like.delete()
            return redirect('posts:home')
        elif form.is_valid():
            form.save()
            # redirect to a new URL:
            return redirect('posts:home')

    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewLikeForm()
    
    return render(request, 'home.html')


#Comment view
@login_required
def new_comment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        # create a form instance and populate it with data from the request:
        form = NewCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            form.save()
            # redirect to a new URL:
            return redirect('posts:home')
    else:
        # if a GET (or any other method) we'll create a blank form
        form =NewCommentForm()
    return redirect('posts:home')

