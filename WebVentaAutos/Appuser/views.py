from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm


# Create your views here.

def register(request):

    if request.method =="POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appuser/inicio.html", {"mensaje": "Usuario creado correctamente!"})
        else:
            return render(request, "Appuser/register.html", {"form": form, "mensaje":"Error al crear el usuario"})            

    else:
        form = RegistroUsuarioForm()
        return render (request, "Appuser/register.html", {"form": form})

