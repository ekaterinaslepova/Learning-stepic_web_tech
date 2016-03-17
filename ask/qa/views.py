from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse, HttpResponseNotFound
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfound(request, *args, **kwargs):
    return HttpResponseNotFound('Page not found')