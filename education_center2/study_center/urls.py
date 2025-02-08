from django.urls import path
from .views import index, course_detail, student_detail

urlpatterns = [
    path('', index),
    path('course/<int:course_id>', course_detail, name="course_detail"),
    path('student/<int:student_id>', student_detail, name="student_detail")
]