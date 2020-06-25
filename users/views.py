"""Users views Configuration"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile, Follow
from posts.models import Post, Like
from django.db import IntegrityError
from .forms import SignUpForm, UpdateProfileForm
from django.urls import reverse


# Login view
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            # Redirect to a success page.
            return redirect('posts:home')
        else:
            # No backend authenticated the credentials
            return render(request, 'users/login.html', {'error': 'La contraseña o el nombre de usuario son incorrectos.'})
    return render(request, 'users/login.html')


#Logout view
@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('users:login')


#Signup view
def signup_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        #import pdb; pdb.set_trace()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('users:login')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form':form})


#Update profile view
@login_required
def update_profile(request):
    #notifications for the navigation bar
    likes = list_notifications(request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpdateProfileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            if data['picture']:
                request.user.profile.picture = data['picture']
            else:
                request.user.profile.picture
            request.user.profile.website = data['website']
            request.user.profile.biography = data['biography']
            request.user.profile.phone = data['phone']
            #request.user.profile.gender = data['gender']
            request.user.profile.save()
            # redirect to a new URL:
            return redirect('users:update-profile')
        else:
            return render(request, 'users/update_profile.html', {'form':form, 'likes':likes})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateProfileForm()      
    return render(request, 'users/update_profile.html', {'likes':likes})


#Profile view 
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    try:
        follow = Follow.objects.get(follower=request.user, followed=user)  
    except Follow.DoesNotExist:
        follow = Follow()
    user.posts = Post.objects.filter(user=user).order_by('-created')
    user.n_posts = Post.objects.filter(user=user).count()
    user.n_followers = Follow.objects.filter(followed=user).count()
    user.n_followed = Follow.objects.filter(follower=user).count()
    user.follow = Follow.objects.filter(follower=request.user, followed=user)
    #notifications for the navigation bar
    likes = list_notifications(request)

    context = {'user':user, 'likes':likes}

    return render(request, 'users/profile.html', context)
                 

#Follow view
@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)
    #import pdb; pdb.set_trace()

    is_already_followed = Follow.objects.filter(follower=request.user, followed=user)
    is_auto_follower = Follow.objects.filter(follower=request.user, followed=request.user)

    if not is_already_followed or is_auto_follower:

        follow = Follow.objects.create(
            followed = user,
            follower = request.user
        )

    else:
        follow = Follow.objects.get(follower=request.user, followed=user)

    url = reverse('users:profile', kwargs={'username':user.username})
    return redirect(url)
   

#Unfollow view
@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(followed=user, follower=request.user)
    follow.delete()

    url = reverse('users:profile', kwargs={'username':user.username})
    return redirect(url)


#Followers view
@login_required
def followers(request, username):
    followers=[]
    user = get_object_or_404(User, username=username)
    follows = Follow.objects.filter(followed=user).order_by('-created')
    
    #notifications for the navigation bar
    likes = list_notifications(request)
    
    for follow in follows:
        followers.append(follow.follower)

    for user in followers:
        user.follow = Follow.objects.filter(followed=user, follower=request.user)

    context= {
            'user':user,
            'contacts':followers,
            'label':'Seguidores',
            'likes':likes
        }
    return render(request,'users/contacts.html', context)


#Followed view
def followed(request, username):
    followed=[]
    user = get_object_or_404(User, username=username)
    follows = Follow.objects.filter(follower=user).order_by('-created')

    for follow in follows:
        followed.append(follow.followed)
    #import pdb; pdb.set_trace()

    #notifications for the navigation bar
    likes = list_notifications(request)

    for user in followed:
        user.follow = Follow.objects.filter(followed=user, follower=request.user)

    user.follow = Follow.objects.filter(followed=user, follower=request.user)

    context= {
        'user':user,
        'contacts':followed, 
        'label':'Seguidos',
        'likes':likes
        }
    return render(request, 'users/contacts.html', context)


#Search-user view
def search(request):
    if request.method == 'POST':
        username_input = request.POST['username']

        results = User.objects.filter(username__contains=username_input)

        #notifications for the navigation bar
        likes = list_notifications(request)

         
        context= {
            'contacts':results,
            'label': 'Resultados de la busqueda "{}"'.format(username_input),
            'likes':likes
         }

        return render(request, 'users/contacts.html', context)


#List likes to the user posts
def list_notifications(request):
    likes = Like.objects.filter(post__profile__user=request.user).exclude(user=request.user).order_by('-created')
    for like in likes:
        like.profile = Profile.objects.get(user=like.user)
    #import pdb; pdb.set_trace()
    return likes


