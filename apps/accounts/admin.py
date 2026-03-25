from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('full_name', 'phone', 'role', 'school', 'is_active')
    list_filter = ('role', 'school', 'is_active')
    search_fields = ('full_name', 'phone')
