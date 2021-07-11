from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage(/)")
    return render(request, 'home.html')

def events(request):
    #return HttpResponse("This is my events page(events)")
    return render(request, 'about.html')

def gallery(request):
    #return HttpResponse("This is gallery page(gallery)")
    return render(request, 'projects.html')

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
       # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been updated in db")
    #return HttpResponse("This is my contact page(contact)")
    return render(request, 'contact.html')
