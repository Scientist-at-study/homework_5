from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, Student

# Register your models here.

admin.site.register(Course)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrolled_at', 'course', 'get_image',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_editable = ('course',)
    readonly_fields = ('get_image',)
    list_per_page = 10
    list_max_show_all = 10

    def get_image(self, student):
        if student.photo:
            image_url = student.photo.url
        else:
            image_url = "https://demofree.sirv.com/nope-not-here.jpg"
        return mark_safe(f'<img src="{image_url}" width="150"')

    get_image.short_description = "Rasmi"


admin.site.register(Student, StudentAdmin)
