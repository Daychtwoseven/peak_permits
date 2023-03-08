from django.shortcuts import render


def index_page(request):
    try:
        return render(request, 'frontend/views/index.html')
    except Exception as e:
        print(e)