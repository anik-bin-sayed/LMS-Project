from django.contrib import admin

from .models import User

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ["id", "username", "email","role","password"]
    ordering = ["id"]
