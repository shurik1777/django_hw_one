import logging
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Client

logger = logging.getLogger(__name__)


def new_page(request):
    context = {
        "title": "Главная страница",
    }
    logger.info("Index page accessed")
    return render(request, "hw_logik_and_template/pre.html", context)


def users(request):
    clients = Client.objects.all()
    context = {
        "title": "Список всех клиентов",
        "clients": clients,
    }
    return render(request, "hw_logik_and_template/users.html", context)


def orders(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    orders = Order.objects.filter(client=client)
    today = timezone.now()

    # Фильтрация заказов по периодам
    orders_week = orders.filter(date_of_order__gte=today - timedelta(days=7)).order_by('-date_of_order')
    orders_month = orders.filter(date_of_order__gte=today - timedelta(days=30)).order_by('-date_of_order')
    orders_year = orders.filter(date_of_order__gte=today - timedelta(days=365)).order_by('-date_of_order')

    context = {
        "title": f"Заказы клиента {client.name}",
        "client": client,
        "orders_week": orders_week,
        "orders_month": orders_month,
        "orders_year": orders_year,
    }
    return render(request, "hw_logik_and_template/orders.html", context)
