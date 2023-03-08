from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from . models import *


def index_page(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            project_address = request.POST.get('project_address')
            project_documents = request.FILES.getlist('project_documents')

            permit = Permit.objects.create(name=name, email=email, phone_number=phone_number, project_address=project_address)
            for i in project_documents:
                fs = FileSystemStorage()
                name = fs.save(i, i)
                PermitFiles.objects.create(permit=permit, document=fs.url(name))

        for row in PermitFiles.objects.all():
            print(row.document)
        return render(request, 'frontend/views/index.html')
    except Exception as e:
        print(e)