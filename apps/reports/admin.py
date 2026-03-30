from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.urls import reverse
from .models import ReportCard

@admin.register(ReportCard)
class ReportCardAdmin(ModelAdmin):
    list_display = ('student', 'term', 'download_pdf_link')
    list_filter = ('term',)

    def download_pdf_link(self, obj):
        url = reverse('reports:download_pdf', args=[obj.id])
        return format_html('<a href="{}" class="button" target="_blank">Download PDF</a>', url)
    
    download_pdf_link.short_description = 'Download'
