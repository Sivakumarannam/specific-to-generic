from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def virat(request):
    return HttpResponse('<h1>50 th Century Im Semis</h1>')
def sheryas(request):
    return HttpResponse('<h1>Sheryas Scored Century in Semis</h1>')
