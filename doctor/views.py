from django.shortcuts import render
from .models import *

# Create your views here.
def doctors(request, id):
    queryset = Doctors.objects.get(id = id)

    return render(request, "doctor.html", {"queryset": queryset})


def department(request, id):
    queryset = Department.objects.get(id = id)

    return render(request, "department.html", {"queryset": queryset})