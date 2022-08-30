from django.contrib.contenttypes import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView


def mainpage(request):
    return render(request, 'travel_app/begreen/index.html')


def activepage(request):
    return render(request, 'travel_app/begreen/activelist.html')

def about_us(request):
    return render(request, 'travel_app/begreen/about-us.html')

def transport(request):
    return render(request, 'travel_app/begreen/transport.html')

def important(request):
    return render(request, 'travel_app/begreen/attention.html')

def goriIPoseleniya(request):
    return render(request, "travel_app/begreen/active1.html")

def kanyon(request):
    return render(request, "travel_app/begreen/sulak-kanyon.html")

def don(request):
    return render(request, "travel_app/begreen/don.html")

def don1(request):
    return render(request, "travel_app/begreen/don1.html")

def kvadro3(request):
    return render(request, "travel_app/begreen/kvadro3.html")