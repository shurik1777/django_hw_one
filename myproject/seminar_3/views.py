from django.shortcuts import render


def index(request):
    return render(request, 'seminar_3/index.html')


def about(request):
    return render(request, 'seminar_3/about.html')
