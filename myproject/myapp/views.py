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

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = "Priyanshu"
    msg = "how are you ?"
    fruits = ["banana","apple","kiwi","Guava"]
    num1=10
    num2=20
    ans= num1>num2
    mydictionary={
        "var" :var,
        "greeting" :msg,
        "myfruits" : fruits,
        "num1" :num1,
        "num2" :num2,
        "ans"  :ans
        
    }
    return render(request,'third.html',mydictionary)
