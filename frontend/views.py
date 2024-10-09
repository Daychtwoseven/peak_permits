from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from . models import *


def index_page(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            permit = Permit.objects.create(name=name, email=email, phone_number=phone_number)
            if permit:
                #request.session['statusMsg'] = True
                return redirect('/#permit-submitter')
        return render(request, 'frontend/views/index.html')
    except Exception as e:
        print(e)


@login_required
def dashboard_page(request):
    try:
        print('here')
    except Exception as e:
        print(e)


@login_required
def request_page(request):
    try:
        return render(request, 'frontend/views/request.html')
    except Exception as e:
        print(e)


def login_page(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('frontend-request-page')  # Redirect to a success page
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'frontend/base/login.html')
    except Exception as e:
        print(e)