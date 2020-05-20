"""Users forms"""

from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(max_length=70, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    phone = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Número telefónico'}))
    username = forms.CharField(max_length=70, min_length=2, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50,  widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password_confirmation = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))
    