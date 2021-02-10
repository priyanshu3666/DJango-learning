from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .forms import  *

# Create your  views here.
def myfunctioncall(request):
    return HttpResponse("hello, this is my localhost page")

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

def myimagepage(request):
    return render(request,'image.html')

def myimagepage2(request):
    return render(request,'image2.html')

def myimagepage3(request):
    return render(request,'image3.html')

def myimagepage4(request,imagename):
    myimagename = imagename
    myimagename = myimagename.lower()
    if myimagename == "re":
        var =True
    elif myimagename == "road":
        var = False
    mydictionary = {
        "var" : var

    }
    return render(request,'image4.html',context=mydictionary)

def myform(request):
    return render(request,'form.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)

def myform2(request):
    
    if request.method == "POST" :
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary ={
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            if  not re.search(regex,email):
                errorflag = True
                errormsg = "Email is not valid "
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary["success"] =  True
                mydictionary["successmsg"] = "Form Submitted"
            mydictionary["error"]= errorflag
            mydictionary["errors"] = Errors
            return render(request,'form2.html',context=mydictionary)
               
    elif request.method == "GET" :
        form = FeedbackForm()
        mydictionary={
            "form":form
        }
        return render(request,'form2.html',context=mydictionary)

def error_404_view(request,exception):
    return render(request,'404.html')