from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Subject, Term, Grade

@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)

@admin.register(Term)
class TermAdmin(ModelAdmin):
    list_display = ('name', 'school')

@admin.register(Grade)
class GradeAdmin(ModelAdmin):
    list_display = ('student', 'subject', 'term', 'score')
    list_filter = ('term', 'subject')
