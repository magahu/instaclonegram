"""Users forms"""

from django import forms
from .models import Profile
from django.contrib.auth.models import User


#Signup Form
class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(max_length=70, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    phone = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Número telefónico'}))
    username = forms.CharField(max_length=70, min_length=2, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50,  widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password_confirmation = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    def clean_username(self):
        #Validate that there's no a repeat username in the signup form
        username = self.cleaned_data['username']
        username_queryset = User.objects.filter(username=username).exists()
        if username_queryset:
            raise forms.ValidationError('Nombre de usuario no disponible', code='invalid_username')
        return username

    def clean(self):
        #Validate password using password_confirmation
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden', code='invalid_password')
        return cleaned_data

    def save(self):
        #Save profile and user data
        data = self.cleaned_data
        data.pop('password_confirmation')
        #user = User.objects.create_user(**data)
        user  = User.objects.create_user(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        email=data['email'],
                        password=data['password']
                        )
        profile = Profile(user=user)
        profile.phone = data['phone']
        profile.save()
    

#Update-profile Form
class UpdateProfileForm(forms.Form):
    picture = forms.ImageField(required=False)
    website = forms.CharField(max_length=70, required=False)
    biography = forms.CharField(max_length=500, widget=forms.Textarea(), required=False)
    phone = forms.CharField(max_length=10, required=False)
    #gender = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.RadioSelect)
