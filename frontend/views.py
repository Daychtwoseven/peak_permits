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