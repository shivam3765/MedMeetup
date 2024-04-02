from django.db import models
from doctor.models import *

class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_age = models.IntegerField(default=15)
    patient_mobile = models.CharField(max_length=15)
    patient_email = models.EmailField()

    def __str__(self) -> str:
        return self.patient_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name="patient", on_delete=models.CASCADE)
    department_name = models.CharField(max_length=30)
    doctor_name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    username = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.patient.patient_name
    
    class Meta:
        unique_together = ['patient', 'date']