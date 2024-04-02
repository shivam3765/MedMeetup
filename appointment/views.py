from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from doctor.models import *
from appointment.models import *

# Create your views here.

@login_required(login_url='/auth/signin')
def appointment(request):
    doctors = Doctors.objects.all()
    departments = Department.objects.all()

    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        patient_age = request.POST.get("patient_age")
        patient_email = request.POST.get("patient_email")
        patient_mobile = request.POST.get("patient_mobile")
        date = request.POST.get('date')
        doctor = request.POST.get('doctor')
        department = request.POST.get('department')
        username = request.user.username


        if not Appointment.objects.filter(patient__patient_name = patient_name, 
                                          date = date, 
                                          patient__patient_mobile=patient_mobile).exists():
            
            patient = Patient.objects.create(
                patient_name = patient_name,
                patient_age = patient_age,
                patient_email = patient_email,
                patient_mobile = patient_mobile,
            )
            patient.save()

            patient = Appointment.objects.create(
                patient = patient,
                date = date,
                doctor_name = doctor,
                department_name = department,
                username = username
            )

            patient.save()

            messages.success(request, "Appointment Successfully Submitted.")
            return redirect("/appointment/appoint/")
        
        messages.info(request, "Patient Already Appointed.")
        return redirect("/appointment/appoint/")
    
    return render(request, "appointment.html", {'doctors': doctors, 'departments': departments})