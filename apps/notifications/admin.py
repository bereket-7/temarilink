from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SMSMessage

@admin.register(SMSMessage)
class SMSMessageAdmin(ModelAdmin):
    list_display = ('phone', 'school', 'status', 'created_at')
    list_filter = ('status', 'school')
    search_fields = ('phone', 'message')
    readonly_fields = ('created_at',)
