from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Fee, Payment

@admin.register(Fee)
class FeeAdmin(ModelAdmin):
    list_display = ('student', 'amount', 'status', 'due_date')
    list_filter = ('status', 'due_date')

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('fee', 'amount', 'paid_at')
    readonly_fields = ('paid_at',)
