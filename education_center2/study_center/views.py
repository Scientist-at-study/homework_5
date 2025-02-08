from django.shortcuts import render
from django.http import (HttpRequest, HttpResponse)
from .models import Course, Student


# Create your views here.


def index(request:HttpRequest):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        "courses": courses,
        "students": students
    }
    return render(request, "index.html", context)

def course_detail(request:HttpRequest, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(course=course)
    context = {
        "course": course,
        "students": students
    }
    return render(request, "course_detail.html", context)


def student_detail(request:HttpRequest, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        "student": student
    }
    return render(request, "student_detail.html", context)