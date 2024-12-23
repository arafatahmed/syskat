from django.shortcuts import render, get_list_or_404, redirect
from .models import Main

# Create your views here.


def home(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/home.html', {'site':site })

def about(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site':site })