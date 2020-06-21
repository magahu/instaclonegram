"""Posts views Configuration"""

from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewLikeForm, NewCommentForm, SavedPostForm 
from posts.models import Post, Like, Comment, SavedPost
from django.urls import reverse
from django.contrib.auth.models import User


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
def home(request):
   
    posts = Post.objects.all().order_by('-posted')
    for post in posts:
        post.like = post.like_set.filter(user=request.user, post=post)
        
         
    #import pdb; pdb.set_trace()
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
            url = reverse('posts:show-comments', kwargs={'pk':post})
            return redirect(url)

    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewLikeForm()
    
    return render(request, 'home.html')


#Create comment view
@login_required
def new_comment(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        #import pdb; pdb.set_trace()
        # create a form instance and populate it with data from the request:
        form = NewCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            form.save()
            # redirect to a new URL:
            post = get_object_or_404(Post, pk=pk)
            url = reverse('posts:show-comments', kwargs={'pk':post.pk})
            return redirect(url)
            
    else:
        # if a GET (or any other method) we'll create a blank form
        form =NewCommentForm()
    return redirect('posts:home')


#Show comments
@login_required
def list_comments(request, pk):
    post = Post.objects.get(pk=pk)
    post.like = post.like_set.filter(user=request.user)

    return render(request, 'posts/comments.html', {'post':post})


#Display users likes
@login_required
def list_likes(request, pk):
    users = []
    likes = Like.objects.filter(post=pk)
    for like in likes:
        user = like.user
        users.append(user)    
    
    return render(request, 'users/contacts.html', {'contacts':users, 'label':'Me gusta'})


@login_required
def save_post(request):
    if request.method == 'POST':
        form = SavedPostForm(request.POST)
        post = request.POST['post']
        user = request.POST['user']

        saved_post = SavedPost.objects.filter(user=user, post=post)

        if saved_post:
            saved_post.delete()
            return redirect('posts:home')
        elif form.is_valid():
            form.save()
            return redirect('posts:show-saved')

    else:
        form = SavedPostForm()
        return redirect('posts:home', {'form':form})


@login_required
def list_saved_posts(request):
    posts = []
    saved = SavedPost.objects.filter(user=request.user)
    for save in saved:
        post = Post.objects.get(pk=save.post.pk)
        posts.append(post)
    
    return render(request, 'posts/saved_posts.html', {'saved_posts':posts})


    
 