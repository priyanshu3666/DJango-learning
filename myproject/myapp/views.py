from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your 
# views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("about responses")

def add(request,a,b):   
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)