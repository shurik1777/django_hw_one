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
