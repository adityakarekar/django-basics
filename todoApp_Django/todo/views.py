from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Task

def task_list(request):
       task=Task.objects.all().order_by('-created_at')
       return render(request,'todo/task_list.html',{'tasks':task})


def add_task(request):
       if request.method=="POST":
              title=request.POST.get('title','').strip()
              description=request.POST.get('description','').strip()
       
              if title:
                     Task.objects.create(title=title,description=description)
                     return redirect(reverse('todo:task_list'))
              error="title cannot be empty."
              return render(request,'todo/task_form.html',{"error":error})
       return render(request,'todo/task_form.html')

def edit_task(request,edit_id):
       task=get_object_or_404(Task,id=edit_id)
       if request.method=="POST":
              title=request.POST.get('title','').strip()
              description=request.POST.get('description','').strip()
              completed=request.POST.get("completed")=="on"
              if title:
                     task.title=title
                     task.description=description
                     task.completed=completed
                     task.save()
                     return redirect(reverse('todo:task_list'))
              return render(request,"todo/task_form.html",{'task':task,"error":"Title cannot be empty"})
       return render(request,"todo/task_form.html",{'task':task})
 
 
def delete_task(request,delete_id):
       task=get_object_or_404(Task,id=delete_id)
       if request.method=="POST":
              task.delete()
              return redirect(reverse('todo:task_list')) 
       return render(request,'todo/task_confirm_delete.html',{"task":task})   

def toggle_task(request, toggle_id):
    task = Task.objects.get(id=toggle_id)
    task.completed = not task.completed
    task.save()
    return redirect("/")                
