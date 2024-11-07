from django.contrib import admin
from .models import Faculty, Group, Department, Student, Subject, Teacher

from django.contrib import admin
from .models import Faculty, Group, Department, Student, Subject, Teacher

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    search_fields = ('name',)
    list_filter = ('faculty',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'department')
    search_fields = ('first_name', 'last_name')
    list_filter = ('group', 'department')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name',)
    list_filter = ('department',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')
    search_fields = ('first_name', 'last_name')
    list_filter = ('subject',)
