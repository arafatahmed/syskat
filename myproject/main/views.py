from django.shortcuts import render, get_list_or_404, redirect
from .models import Main
from news.models import News

# Create your views here.


def home(request):

    site = Main.objects.get(pk=1)
    news = News.objects.all()


    return render(request, 'front/home.html', {'site':site, 'news':news })

def about(request):

    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site':site })