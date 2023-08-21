from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable':'hii this is varibale value is a575',
        'variable1':'hii this is varibqle two'
    }
   # messages.success(request, " Your response has been submitted .. Wait for sometime i will contact you soon")

    return render(request,'index.html',context)
    # return HttpResponse("this is home pAge  and i make i=this page ")

# about page
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about paag3e  and  in this all the content about the about section ")

# services page
def services(request):
    return render(request, 'service.html')
   #return HttpResponse("this is servie page ")

# contact page
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your response has been submitted !! Please Allow Sometime I Will be in  Contact With You Shortly!!! Thank You!!')
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page  ")