from .models import Task

from django.contrib import admin

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','completed','created_at')
    list_filter=('completed','created_at')
    search_fields=('title','description')
    ordering=('-created_at',)
    
