

from django.contrib import admin
from .models import Student,Profile

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("name","age","city")
    search_fields=("name","city")
    list_filter=("age","city")
    ordering=("name",)
    
    
@admin.register(Profile)
class StudentAdmin(admin.ModelAdmin):
    list_display=("bio","location","birth_date")
    search_fields=("bio","location")
