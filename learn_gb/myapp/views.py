import random
from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    logger.info('about page accessed')
    return HttpResponse("Hello, world. You're at the polls index.")


def random_coin(request):
    result = random.choice(['Орел', 'Решка'])
    return HttpResponse(f'Результат подбрасывания монет:<h1>{result}</h1>')


def random_number(request):
    result = random.randint(0, 100)
    logger.debug('About page accessed')
    return HttpResponse(f'Случайное число от 0 до 100:<h1>{result}</h1>')


def random_roll(request):
    result = random.randint(1, 6)

    return HttpResponse(f'Случайное число от 1 до 6:<h1>{result}</h1>')
