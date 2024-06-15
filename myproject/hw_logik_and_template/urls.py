from django.urls import path
from . import views

urlpatterns = [
    path('pre/', views.new_page, name='new_page'),
    path('orders/<int:client_id>', views.orders, name='orders'),
    path('orders/', views.orders, name='all_orders'),
]
