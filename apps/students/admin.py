from django.contrib import admin
from .models import Student, Guardian

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'grade', 'section', 'school')
    list_filter = ('school', 'grade')
    search_fields = ('full_name',)

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'student')
    search_fields = ('full_name', 'phone')
