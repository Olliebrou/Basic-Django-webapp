from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def onlinestore(request):
    return render(request, "onlinestore.html")

def CV (request):
    return render(request, "CV.html")

# Create your views here.
