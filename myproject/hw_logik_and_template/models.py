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
