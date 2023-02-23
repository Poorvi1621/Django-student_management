from django.contrib import admin
from .models import AddCourses
from .models import AddStudents
from .models import AddTeacher
admin.site.register(AddCourses)
admin.site.register(AddStudents)
admin.site.register(AddTeacher)