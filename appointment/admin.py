from django.contrib import admin
from .models import *

class patientAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_age', 'patient_email', 'patient_mobile']
admin.site.register(Patient, patientAdmin)


class appointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'department_name', 'doctor_name', 'date', 'username']
admin.site.register(Appointment, appointmentAdmin)