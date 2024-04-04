from django.shortcuts import render
from .models import *


# ======================== This function show the doctors details =======================
def doctors(request, id):
    queryset = Doctors.objects.get(id = id)

    return render(request, "doctor.html", {"queryset": queryset})


# ======================== This function show the department details =======================
def department(request, id):
    queryset = Department.objects.get(id = id)

    return render(request, "department.html", {"queryset": queryset})