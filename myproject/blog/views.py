from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Blog Home Page!")


def about(request):
    return HttpResponse("This is the About Page of the Blog.")
