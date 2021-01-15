from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    context = {}
    return render(request, 'user/index.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        password = request.POST.get('password', False)    
        username = request.POST.get('username', False)
        print(username, password)
        
        user = authenticate(request, username=username, password=password)
        print(user)
        print(User.objects.filter(username=username), user)
        if user:
            print(user)
            login(request, user)
            return redirect("user:index")
        else:
            messages.error(request, "Username or password is incorrect...")
            return redirect("user:login")

    else:
        context = {}
        return render(request, 'user/login.html',context)

def signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password1', False)    
        confirm_password = request.POST.get('password2', False)

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Thsi username is already taken...')
                return redirect('user:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"This email is already registered...")
                return redirect('user:signup')
            else:
                user = User.objects.create(first_name=first_name, last_name= last_name, username=username, email=email, password=make_password(password))
                user.save()
                messages.info(request, "user created successfully. Please Login to continue...")
                return redirect('user:login')
        else:
            messages.error(request,"Password does not match...")
            return redirect('user:signup')
    else:
        context = {}
        return render(request, 'user/signup.html',context)

def logout(request):
    auth.logout(request)
    return redirect("user:index")