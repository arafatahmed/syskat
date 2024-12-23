from django.shortcuts import render, get_list_or_404, redirect
from .models import News

# Create your views here.


def listnews(request):

    site = News.objects.get(pk=1)

    return render(request, 'front/listnews.html', {'site':site })