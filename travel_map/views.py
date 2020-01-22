from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'travel_map/Index.html')


def register(request):
    return render(request, 'travel_map/Index.html')
