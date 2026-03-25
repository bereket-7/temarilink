from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Student, Guardian

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ('full_name', 'grade', 'section', 'school')
    list_filter = ('school', 'grade')
    search_fields = ('full_name',)

@admin.register(Guardian)
class GuardianAdmin(ModelAdmin):
    list_display = ('full_name', 'phone', 'student')
    search_fields = ('full_name', 'phone')
