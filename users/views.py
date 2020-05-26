"""Users views Configuration"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
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
    return redirect('login')


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
            return redirect('login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form':form})


#Update profile view
@login_required
def update_profile(request):
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
            return redirect('update-profile')

        else:
            return render(request, 'users/update_profile.html', {'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateProfileForm()
         
    return render(request, 'users/update_profile.html')


#Profile view
@login_required
def profile(request):
    return render(request, 'users/profile.html')
    #return render(reverse('profile'))