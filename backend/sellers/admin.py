from django.contrib import admin
from sellers.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


# Register your models here.
class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'nick', 'first_name',)
    list_filter = ('email', 'nick', 'first_name', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('nick', 'first_name', 'phone', 'email',
                    'is_active', 'is_staff')
    fieldsets = (
        (None,
         {'fields': ('email', 'nick', 'first_name', 'second_name', 'last_name', 'profile_photo', 'phone', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }


admin.site.register(CustomUser, UserAdminConfig)