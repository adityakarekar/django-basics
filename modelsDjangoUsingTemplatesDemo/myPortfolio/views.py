from django.shortcuts import render
from myPortfolio.models import Student

def student_list(request):
    students=Student.objects.all()
    return render(request,'portfolio/students_list.html',{"students":students})
