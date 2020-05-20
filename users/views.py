"""Users views Configuration"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db import IntegrityError
from .forms import SignUpForm

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # No backend authenticated the credentials
            return render(request, 'users/login.html', {'error': 'La contraseña o el nombre de usuario no son correctos.'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):

    logout(request)
    # Redirect to a success page.
    return redirect('login')


def signup_view(request):
    #import pdb; pdb.set_trace()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            try:
                data = form.cleaned_data
                first_name = data['first_name']
                last_name = data['last_name']
                email = data['email']
                username = data['username']
                password = data['password']
                password_confirmation = data['password_confirmation']
                if password == password_confirmation:
                    user  = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                        )
                    profile = Profile(user=user)
                    profile.phone = data['phone']
                    profile.save()
                    # redirect to a new URL:
                    return redirect('login')
                else:
                    return render(request, 'users/signup.html', {'form':form})
            except IntegrityError:
                return render(request, 'users/signup.html', {'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form':form})