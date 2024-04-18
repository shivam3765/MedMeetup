from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# ==================== This function use for SignUp  ==================
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check for empty fields
        if not all([first_name, last_name, email, username, password]):
            messages.info(request, "All fields are required.")
            return redirect("/auth/signup")

        # Validate username format
        import re
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            messages.info(request, "Username can only contain letters (a-z or A-Z), numbers (0-9), and underscores (_).")
            return redirect("/auth/signup")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists.")
            return redirect("/auth/signup")

        # Create user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account successfully created.")
        return redirect('/auth/signup')

    return render(request, "registration.html")



# ======================= This function for SignIn =================================
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


# ========================= This function for SignOut =====================
def signout(request):
    logout(request=request)

    return redirect("/")