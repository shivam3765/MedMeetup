from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect("/auth/signup")
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.success(request, "Account Successfully created.")
        return redirect('/auth/signup')

    return render(request, "registration.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_exist = User.objects.filter(username = username).exists()

        if not user_exist:
            messages.info(request, "Invalid username.")
            return redirect('/auth/signin')
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/auth/signin')
        
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def signout(request):
    logout(request=request)

    return redirect("/")