from django.shortcuts import render


def index(request):
    return render(request, 'library/index.html', {'x': 500})