from django.shortcuts import render


def index_main(request):
    return render(request, 'main/index.html')


def about_main(request):
    return render(request, 'main/about.html')
