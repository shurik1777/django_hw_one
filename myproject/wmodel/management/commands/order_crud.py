from django.core.management.base import BaseCommand
from myproject.wmodel.models import Order, Client, Article


class Command(BaseCommand):
    help = 'Manage orders'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='subcommand')

        parser_create = subparsers.add_parser('create', help='Создать новый заказ')
        parser_create.add_argument('--client_id', type=int, help='Идентификатор клиента')
        parser_create.add_argument('--article_id', type=int, help='Идентификатор заказа')
        parser_create.add_argument('--price', type=float, help='Стоимость заказа')
        parser_create.add_argument('--date_of_decor', type=str, help='Дата оформления')

        parser_update = subparsers.add_parser('update', help='Обновить информацию по заказу')
        parser_update.add_argument('--order_id', type=int, help='Идентификатор заказа для обновления')
        parser_update.add_argument('--client_id', type=int, help='Новый идентификатор клиента')
        parser_update.add_argument('--article_id', type=int, help='Новый идентификатор заказа')
        parser_update.add_argument('--price', type=float, help='Цена нового заказа')
        parser_update.add_argument('--date_of_decor', type=str, help='Новая дата оформления')

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
        client = Client.objects.get(id=options['client_id'])
        article = Article.objects.get(id=options['article_id'])
        order = Order(
            client=client,
            article=article,
            price=options['price'],
            date_of_decor=options['date_of_decor']
        )
        order.save()
        self.stdout.write(self.style.SUCCESS('Заказ успешно создан'))

    def handle_update(self, **options):
        order = Order.objects.get(id=options['order_id'])
        client = Client.objects.get(id=options['client_id']) if options['client_id'] else order.client
        article = Article.objects.get(id=options['article_id']) if options['article_id'] else order.article
        order.client = client
        order.article = article
        order.price = options['price'] if options['price'] else order.price
        order.date_of_decor = options['date_of_decor'] if options['date_of_decor'] else order.date_of_decor
        order.save()
        self.stdout.write(self.style.SUCCESS('Заказ успешно обновлен'))

    def handle_list(self):
        orders = Order.objects.all()
        for order in orders:
            print(f"{order.id}: {order.client}, {order.article}, {order.price}")

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
                              f"Товар: {order.client}\n"
                              f"Описание: {order.article}\n"
                              f"Цена: {order.price}\n"
                              f"Дата реализации: {order.date_of_decor}")
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором: {order_id} не существует.'))

# py manage.py order_crud update --order_id 1 --client_id 1 --article_id 2 --price 7 --date_of_decor "2024-06-10"
# py manage.py order_crud list
# py manage.py order_crud delete --order_id 1
# py manage.py order_crud get --order_id 1
