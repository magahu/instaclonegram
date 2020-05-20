"""users views Configuration"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db import IntegrityError

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
    #simport pdb; pdb.set_trace()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error':'La contraseña que ingresate no coincide'})
    
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            profile = Profile(user=user)
            profile.phone = request.POST['phone']
            profile.save()
            return redirect('login')

        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'Nombre de usuario no disponible'}) 

    return render(request, 'users/signup.html')