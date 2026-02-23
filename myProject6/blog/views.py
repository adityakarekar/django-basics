from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request,"home.html")

def blog_details(request):
    post={
        "title":"My #2 Templates Post",
        "description":"Dummy descrription",
        "author":"no",
        "created_at":datetime(2025,8,19,10,3),
        "comments_count":5,
        "price":100,
        "number":2,
        "tags":["Django","Python"]
    }
    return render(request,"blog/blog_details.html",{"post":post})
