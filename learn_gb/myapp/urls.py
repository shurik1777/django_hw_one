from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('random_coin/', views.random_coin, name='random_coin'),
    path('random_number/', views.random_number, name='random_number'),
    path('random_roll/', views.random_roll, name='random_roll'),
]
