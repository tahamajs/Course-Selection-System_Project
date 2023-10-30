from django.contrib import admin
from shared.admin import *
from .models import *

admin.site.register(Faculty, GeneralAdmin)
admin.site.register(FieldOfStudy, GeneralAdmin)
admin.site.register(Term, GeneralAdmin)
