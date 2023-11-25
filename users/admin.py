from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class CustomUserAdmin(UserAdmin):
    # Customize how CustomUser model is displayed in admin
    # Example:
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('user_name', 'first_name', 'last_name')}),
        # Add any additional fields here as per your model
    )
    add_fieldsets = (
        # Configuration for adding a new CustomUser
        # Include required fields for creating a new user
    )
    list_display = ('email', 'user_name', 'first_name', 'last_name')
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    ordering = ('email',)



admin.site.register(CustomUser, CustomUserAdmin)