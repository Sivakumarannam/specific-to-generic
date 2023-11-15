from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def williamson(request):
    return HttpResponse('<h1>Williamson Scored 50th </h1>')

def boult(request):
    return HttpResponse('<h1>Boult Take Today 2 Wickets.</h1>')