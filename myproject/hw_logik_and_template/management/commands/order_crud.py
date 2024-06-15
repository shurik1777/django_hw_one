from decimal import Decimal

from django.core.management.base import BaseCommand
from ...models import Order, Client, Product


class Command(BaseCommand):
    help = 'Manage orders'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='subcommand')

        parser_create = subparsers.add_parser('create', help='Создать новый заказ')
        parser_create.add_argument('--client_id', type=int, help='Идентификатор клиента')
        parser_create.add_argument('--product_id', type=int, help='Идентификатор заказа')
        parser_create.add_argument('--price', type=Decimal, help='Стоимость заказа')
        parser_create.add_argument('--date_of_order', type=str, help='Дата оформления')

        parser_update = subparsers.add_parser('update', help='Обновить информацию по заказу')
        parser_update.add_argument('--order_id', type=int, help='Идентификатор заказа для обновления')
        parser_update.add_argument('--client_id', type=int, help='Новый идентификатор клиента')
        parser_update.add_argument('--product_id', type=int, help='Новый идентификатор заказа')
        parser_update.add_argument('--price', type=Decimal, help='Цена нового заказа')
        parser_update.add_argument('--date_of_order', type=str, help='Новая дата оформления')

        parser_list = subparsers.add_parser('list', help='Список всех заказов')

        parser_delete = subparsers.add_parser('delete', help='Удалить заказ')
        parser_delete.add_argument('--order_id', type=int, help='ID заказа для удаления')
        parser_get = subparsers.add_parser('get', help='Получить информацию о товаре по id')
        parser_get.add_argument('--order_id', type=int, help='Идентификатор товара для получения информации')

    def handle(self, *args, **options):
        if options['subcommand'] == 'create':
            self.handle_create(**options)
        elif options['subcommand'] == 'update':
            self.handle_update(**options)
        elif options['subcommand'] == 'list':
            self.handle_list()
        elif options['subcommand'] == 'delete':
            self.handle_delete(**options)
        elif options['subcommand'] == 'get':
            self.handle_get(**options)

    def handle_create(self, **options):
        client_id = options.get('client_id')
        product_id = options.get('product_id')
        price = options.get('price', None)
        date_of_order = options.get('date_of_order', None)

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором: {client_id} не найден.'))
            return

        try:
            products = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Продукт с идентификатором: {product_id} не найден.'))
            return

        order = Order(
            client=client,
            price=price,
            date_of_order=date_of_order
        )
        order.save()

        # Добавляем продукты к заказу
        order.products.set([products])

        self.stdout.write(self.style.SUCCESS('Заказ успешно создан'))

    def handle_update(self, **options):
        order = Order.objects.get(id=options['order_id'])
        client = Client.objects.get(id=options['client_id']) if options['client_id'] else order.client
        product = Product.objects.get(id=options['product_id']) if options['product_id'] else order.product
        order.client = client
        order.product = product
        order.price = options['price'] if options['price'] else order.price
        order.date_of_order = options['date_of_order'] if options['date_of_order'] else order.date_of_order
        order.save()
        self.stdout.write(self.style.SUCCESS('Заказ успешно обновлен'))

    def handle_list(self):
        orders = Order.objects.all()
        for order in orders:
            print(f"{order.id}: {order.client}, {order.product}, {order.price}")

    def handle_delete(self, **options):
        order_id = options['order_id']
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            self.stdout.write(self.style.SUCCESS(f'Заказ с идентификатором: {order_id} удален.'))
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Заказ с идентификатором: {order_id} не существует.'))

    def handle_get(self, **options):
        order_id = options['order_id']
        try:
            order = Order.objects.get(id=order_id)
            self.stdout.write(f"ID: {order.id}\n"
                              f"Client: {order.client}\n"
                              f"Products: {', '.join([product.title for product in order.products.all()])}\n"
                              f"Price: {order.price}\n"
                              f"Order Date: {order.date_of_order}")
            return  # добавленный return
        except Order.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Order with id: {order_id} does not exist.'))  # исправленный текст ошибки

# py manage.py order_crud create --client_id 1 --product_id 2 --price 8 --date_of_order "2024-06-09"
# py manage.py order_crud update --order_id 1 --client_id 1 --product_id 1 --price 7 --date_of_order "2024-06-10"
# py manage.py order_crud list
# py manage.py order_crud delete --order_id 1
# py manage.py order_crud get --order_id 1
