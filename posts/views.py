"""Posts views Configuration"""

from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewLikeForm, NewCommentForm
from posts.models import Post, Like, Comment
from django.urls import reverse


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


#Create like view
@login_required
def new_like(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewLikeForm(request.POST)
       
        post = request.POST['post']
        user = request.POST['user']
        like = Like.objects.filter(post=post, user=user)
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


#Create comment view
@login_required
def new_comment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        #import pdb; pdb.set_trace()
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


#Show comments
def list_comments(request):
    return render(request, 'posts/comment.html')
    #url = reverse('posts:show-comments', kwargs={'post':post.pk})
    #return redirect(url)
    #comment = Comment.objects.filter(pk=post_id)
    #return render(request, 'comment.html', {'comment':comment})


