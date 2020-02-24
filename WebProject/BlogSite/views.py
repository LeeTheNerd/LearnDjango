from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello Newman</h1>')


def index(request):
    return render(request, 'blogsite/index.html')
