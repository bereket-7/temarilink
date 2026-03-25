from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ReportCard

@admin.register(ReportCard)
class ReportCardAdmin(ModelAdmin):
    list_display = ('student', 'term', 'pdf_url')
    list_filter = ('term',)
