from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deepali(request):
    return HttpResponse('<marquee><h1>can you please come with me to home</marquee></h1>')