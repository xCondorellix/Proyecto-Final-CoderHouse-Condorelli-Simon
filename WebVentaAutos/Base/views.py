from django.shortcuts import render
from Appuser.views import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "Core/home.html")

@login_required
def blog(request):
    return render(request, "Core/blog.html")

def about(request):
    return render(request, "Core/about.html")

