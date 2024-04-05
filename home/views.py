from django.shortcuts import render, redirect
import json
from doctor.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from appointment.models import *

with open("./static/files/data.json") as file:
    data = json.load(file)


# ================= This function Show the Doctors and Departments Details =================
def home(request):
    department = Department.objects.all()
    doctors = Doctors.objects.all()

    return render(request, "home.html" , {"data" : data, "department": department, "doctors": doctors})


# ========================= This function for user query =====================
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        subject = "User query from hospital"
        send_mail(subject=subject,
                message=f"{message} \n\n User name is : {name} \n  User email address is : {email}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=settings.EMAIL_HOST_RESIVER,
                fail_silently=False
                )
        
        messages.success(request, "Message Successfully Send.")
        return redirect("/contact/")
    return render(request, "contact.html")



# ============================== This function for about contant ==============================
def about(request):
    return render(request, "about.html")


# ========================= This function show the user appointment =====================
def show_appointment(request):
    if request.user.is_authenticated:
        user = request.user
        queryset = Appointment.objects.filter(username = user.username).order_by("-date")

    return render(request, "profile.html" , {"user": user, "queryset": queryset})


# ========================= This function show & upload the user profile =====================
def upload_profile_image(request):
    if request.method == 'POST':
        class ProfileImageForm(forms.Form):
            profile = forms.ImageField()

        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.profile_image = form.cleaned_data['profile']
            user_profile.save()
            return redirect('/profile/')
    else:
        form = ProfileImageForm()
    return render(request, 'profile.html', {'form': form})


# ========================= This function for reset password =====================
def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user is not None:
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, "Password Successfully Reset.")
                return redirect('/reset_password/')
            else:
                messages.info(request, "Passwords do not match.")
                return redirect('/reset_password/')
            
        messages.info(request, "Invalid username.")
        return redirect('/reset_password/')
    
    return render(request, "passwordReset.html")