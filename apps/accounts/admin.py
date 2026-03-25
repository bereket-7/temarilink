from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'role', 'school', 'is_active')
    list_filter = ('role', 'school', 'is_active')
    search_fields = ('full_name', 'phone')
