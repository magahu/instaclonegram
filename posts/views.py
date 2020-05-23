"""Posts views Configuration"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from posts.models import Post

#Home view
@login_required
def posts(request):
    posts_queryset = Post.objects.all().order_by('-posted')
    return render(request, 'home.html', {'posts':posts_queryset})


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
            return redirect('home')
    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewPostForm()
    return render(request, 'posts/new_post.html', {'form':form})

