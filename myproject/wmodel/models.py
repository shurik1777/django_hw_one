from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    date_of_register = models.DateField()


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_decor = models.DateField()
   