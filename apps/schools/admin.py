from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import School

@admin.register(School)
class SchoolAdmin(ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)
