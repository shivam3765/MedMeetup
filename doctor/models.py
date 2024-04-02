from django.db import models

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=30)
    doctor_occupation = models.CharField(max_length=50)
    doctor_image = models.ImageField(upload_to="doctors")

    def __str__(self) -> str:
        return self.doctor_name


class Department(models.Model):
    department_name = models.CharField(max_length=20)
    department_description = models.CharField(max_length=500)
    department_image = models.ImageField(upload_to="departments") 


    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department_name']