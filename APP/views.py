from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def homepage(request):
    st = Student.objects.all()
    return render(request, "index.html", {"stu":st})

def addStudent(request):
    return render(request, "addStudent.html")

def addStudentRec(request):
      fn=request.POST["first_name"]
      ln=request.POST["last_name"]
      cn=request.POST["class_name"]
      std=Student(first_name=fn,last_name=ln,class_name=cn)
      std.save()
      return redirect("/")

def delete_student(request,id):
    stdd=Student.objects.get(id=id)
    stdd.delete()
    return redirect("/")
def update(request,id):
    st=Student.objects.get(id=id)
    return render(request,"update.html",{"st":st})

def updateStudent(request,id):
    fn=request.POST["first_name"]
    ln = request.POST["last_name"]
    cn = request.POST["class_name"]
    stu=Student.objects.get(id=id)
    stu.first_name=fn
    stu.last_name=ln
    stu.class_name=cn
    stu.save()
    return redirect("/")