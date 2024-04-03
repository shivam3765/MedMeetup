from django.shortcuts import render, redirect
import json
from doctor.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from appointment.models import *

with open("./static/files/data.json") as file:
    data = json.load(file)


def home(request):
    department = Department.objects.all()
    doctors = Doctors.objects.all()

    return render(request, "home.html" , {"data" : data, "department": department, "doctors": doctors})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        subject = f"{name} quert from your hospital website"
        send_mail(subject=subject,
                message=message,
                recipient_list=[settings.EMAIL_HOST_USER],
                from_email= email,
                fail_silently=False
                )
        
        messages.success(request, "Message Successfully Send.")
        return redirect("/contact/")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        queryset = Appointment.objects.filter(username = user.username).order_by("-date")

    return render(request, "profile.html" , {"user": user, "queryset": queryset})