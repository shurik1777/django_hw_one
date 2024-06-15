from decimal import Decimal

from django.db import models as m


class Client(m.Model):
    """
    name - имя,
    email - эл. почта(уникальна),
    phone - номер телефона
    date_of_register - дата регистрации(автоматически срабатывает если не указать)
    """
    name = m.CharField(max_length=32)
    email = m.EmailField(unique=True)
    phone = m.CharField(max_length=15)
    address = m.CharField(max_length=128)
    date_of_register = m.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(m.Model):
    """
    title - название,
    content - содержание(большое поле для текста),
    price - цена,
    amount - количество,
    date - дата (автоматически срабатывает если не указать)
    """
    title = m.CharField(max_length=128)
    content = m.TextField()
    price = m.DecimalField(max_digits=100, decimal_places=2, default=0)
    amount = m.PositiveIntegerField(default=0)
    date = m.DateField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}, price: {self.price}, amount: {self.amount}"


class Order(m.Model):
    """
    Модель описывает заказ.

    Поля:
    - client: ForeignKey на модель Client, связь многие-к-одному,
        каскадное удаление, связь через related_name 'orders'.
    - products: ManyToManyField на модель Product,
        связь многие-ко-многим, связь через related_name 'orders'.
    - price: DecimalField для хранения цены заказа с максимальным
        количеством цифр 5 и 2 цифрами после запятой.
    - date_of_order: DateField с авто-заполнением текущей даты
        при создании.

    Методы:
    - __str__(self): возвращает строку с описанием заказа.
    - calculate_total_price(self): вычисляет общую стоимость заказа
     на основе цен продуктов и сохраняет результат в total_amount.
    """
    client = m.ForeignKey(Client, on_delete=m.CASCADE, related_name='orders')
    products = m.ManyToManyField(Product, related_name='orders')
    price = m.DecimalField(max_digits=5, decimal_places=2)
    date_of_order = m.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.client.name}"

    def calculate_total_price(self):
        """
        Метод для вычисления общей стоимости заказа
        на основе цен продуктов.
        """
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_amount = total
