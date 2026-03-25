from django.contrib import admin
from .models import Subject, Term, Grade

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'term', 'score')
    list_filter = ('term', 'subject')
