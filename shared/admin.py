from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class GeneralAdmin(BaseUserAdmin):
    search_fields = list_display = ('__all__',)
