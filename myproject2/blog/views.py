from django.shortcuts import render
from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"This is the post details view for post ID: {post_id}")

def user_profile(request, username):
    return HttpResponse(f"This is the user profile view for username: {username}")

def archive_by_year(request, year):
    return HttpResponse(f"This is the archive view for the year: {year}")

def article_details(request,**kwargs):
    return HttpResponse(f"This is the article details view for year: {kwargs.get("year",2026)} and month: {kwargs.get("month",1)}")