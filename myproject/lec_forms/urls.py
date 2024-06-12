from django.urls import path
from .views import user_form, many_fields_form, add_user

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('user/', add_user, name='add_user'),
    path('forms/', many_fields_form, name='many_fields_form'),
]
