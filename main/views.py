from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Main page</h1>")

def wiki(request):
    return HttpResponse("<h1>wiki</h1>")

def updates(request):
    return HttpResponse("<h1>updates</h1>")

def download(request):
    return HttpResponse("<h1>download</h1>")