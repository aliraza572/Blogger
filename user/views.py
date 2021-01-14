from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    context = {}
    return render(request, 'user/index.html',context)

def login(request):
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
                user = User.objects.create(first_name=first_name, last_name= last_name, username=username, email=email, password=password)
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
    pass