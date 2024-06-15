from django.urls import path
from .views import flip_coin, roll_cube, random_number, perform_action

urlpatterns = [
    path('flip/<int:tryes>', flip_coin, name='flip_coin'),
    path('flip_t/<int:tryes>', roll_cube, name='roll_cube'),
    path('flip_r/<int:tryes>', random_number, name='random_number'),
    path('flip_f/', perform_action, name='perform_action'),
]
