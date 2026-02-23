from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def home(request):
    context={
        "name":"Aditya Karekar",
        "age":27,
        "skill":["python","django","fastapi","React"],
        "user":User("Aditya",27),
        "blog":{"title":"Django Templates Intro","content":"<b>This is bold</b>","created_at":datetime(2025,8,18,10,30)},
        "empty_value":None
    }
    return render(request,"home.html",context)
