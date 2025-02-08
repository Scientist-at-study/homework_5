from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Tavsifi")
    photo = models.ImageField(upload_to="course/photos", null=True, blank=True, verbose_name="Rasmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Kurslar'
        verbose_name = 'Kurs'


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    email = models.CharField(max_length=100, verbose_name="Pochta")
    photo = models.ImageField(upload_to="student/photos", null=True, blank=True, verbose_name="Rasmi")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Royhatdan otgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Studentlar'
        verbose_name = 'Student'