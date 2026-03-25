from django.contrib import admin
from .models import ReportCard

@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'pdf_url')
    list_filter = ('term',)
