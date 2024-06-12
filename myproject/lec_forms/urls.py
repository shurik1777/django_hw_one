from django.urls import path
from .views import user_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
]
