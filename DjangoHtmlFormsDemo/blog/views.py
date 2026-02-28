from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def contact_form(request):
    return render(request,"contact.html")
    
def submit_form(request):
    if request.method=="POST":
        _name=request.POST.get("name")
        _message=request.POST.get("message")
        
        if _name and _message:
            Contact.objects.create(name=_name,message=_message)
            return HttpResponse(f"Thank You {_name}. Your message has been recieved")
        else:
            return HttpResponse("Please provide both name and message.")
    
    redirect("contact_form")        


