from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    blogs=[
        {"title":"Django Basics","is_featured":True,"author":"Aditya Karekar"},
        {"title":"Django Advanced","is_featured":False,"author":""},
        {"title":"Django REST Framework (DRF)","is_featured":False,"author":"Dinesh Gandu"}
    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>Welcome to my code</h1>"
    }
    return render(request,"blog/blog_list.html",context)

