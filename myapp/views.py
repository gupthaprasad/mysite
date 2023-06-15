from django.shortcuts import render
from .forms import StudentCF

def home(request):
    return render(request,'myapp/home.html')

def student(request):
    return render(request,'myapp/student.html')

def createstudent(request):
    context={}
    context['form']=StudentCF()
    return render(request,'myapp/createstudent.html',context)

