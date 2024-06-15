import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name}, {email}, {age}.')

    else:
        form = UserForm()
    return render(request, 'lec_forms/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'{form.cleaned_data}')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'lec_forms/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Get {name}, {email}, {age}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранен'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'lec_forms/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'lec_forms/upload_image.html', {'form': form})
