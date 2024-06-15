from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='index_main'),
    path('about/', views.about_main, name='about_main'),
]
