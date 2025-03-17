from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def wiki(request):
    return render(request, "wiki.html")

def updates(request):
    return HttpResponse(request, "updates.html")

def download(request):
    return HttpResponse(request, "download.html")