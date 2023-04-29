from django import forms

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    name=forms.CharField(label= "Nombre usuario")
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

