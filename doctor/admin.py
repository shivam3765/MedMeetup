from django.contrib import admin
from .models import *

class doctorsAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'doctor_occupation']

admin.site.register(Doctors, doctorsAdmin)


admin.site.register(Department)

