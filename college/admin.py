from django.contrib import admin
from shared.admin import *
from .models import *

admin.site.register(Faculty, admin.ModelAdmin)
admin.site.register(FieldOfStudy, admin.ModelAdmin)
admin.site.register(Term, admin.ModelAdmin)
