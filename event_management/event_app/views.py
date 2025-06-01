from django.contrib import messages
from django.shortcuts import render, redirect
from .models import EventRegistration
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def events(request):
    return render(request, 'events.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        eventname = request.POST.get('eventname')
        date = request.POST.get('date')

        if not name or not email or not password or not eventname or not date:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('register')

        if not User.objects.filter(username=name).exists():
            user = User.objects.create_user(username=name, password=password, email=email)
            user.save()
        else:
            messages.error(request, 'Username already exists.')
            return redirect('register')

        registration = EventRegistration(
            name=name,
            email=email,
            phonenumber=phonenumber,
            address=address,
            eventname=eventname,
            date=date
        )
        registration.save()
        return redirect('register_success')
    return render(request, 'register.html')


def register_success(request):
    return render(request, 'register_success.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
