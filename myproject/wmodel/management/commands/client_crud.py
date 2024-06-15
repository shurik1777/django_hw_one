from django.core.management.base import BaseCommand
from myproject.wmodel.models import Client
from django.utils import timezone


class Command(BaseCommand):
    help = 'Manage clients'

    def add_arguments(self, parser):
        subparser = parser.add_subparsers(dest='subcommand')

        parser_create = subparser.add_parser('create', help='Создать нового клиента')
        parser_create.add_argument('--name', type=str, help='Имя клиента')
        parser_create.add_argument('--email', type=str, help='Электронная почта клиента')
        parser_create.add_argument('--phone', type=str, help='Телефон клиента')
        parser_create.add_argument('--address', type=str, help='Адрес клиента')
        parser_create.add_argument('--date_of_register', type=str, help='Дата регистрации',
                                   default=timezone.now().strftime("%Y-%m-%d"))
        parser_update = subparser.add_parser('update', help='Обновить существующего клиента')
        parser_update.add_argument('--client_id', type=int, help='Идентификатор клиента для обновления')
        parser_update.add_argument('--name', type=str, help='Новое имя клиента')
        parser_update.add_argument('--email', type=str, help='Электронная почта нового клиента')
        parser_update.add_argument('--phone', type=str, help='Телефон нового клиента')
        parser_update.add_argument('--address', type=str, help='Адрес нового клиента')
        parser_update.add_argument('--date_of_register', type=str, help='Дата регистрации',
                                   default=timezone.now().strftime("%Y-%m-%d"))

        subparser.add_parser('list', help='Список всех клиентов')

        parser_delete = subparser.add_parser('delete', help='Удалить клиента')
        parser_delete.add_argument('--client_id', type=int, help='Идентификатор клиента, которого нужно удалить')
        parser_get = subparser.add_parser('get', help='Получить информацию о клиенте по id')
        parser_get.add_argument('--client_id', type=int, help='Идентификатор клиента для получения информации')

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
        client = Client(
            name=options['name'],
            email=options['email'],
            phone=options['phone'],
            address=options['address'],
            date_of_register=options['date_of_register'] or timezone.now().strftime("%Y-%m-%d"),
        )
        client.save()
        self.stdout.write(self.style.SUCCESS('Клиент успешно создан'))

    def handle_update(self, **options):
        client_id = options['client_id']
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']
        date_of_register = options['date_of_register'] or timezone.now().strftime("%Y-%m-%d")

        client = Client.objects.get(id=client_id)
        client.name = name
        client.email = email
        client.phone = phone
        client.address = address
        client.date_of_register = date_of_register
        client.save()
        self.stdout.write(self.style.SUCCESS('Клиент обновлен успешно'))

    def handle_list(self):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f"{client.id}: {client.name}, {client.email}")

    def handle_delete(self, **options):
        client_id = options['client_id']
        try:
            client = Client.objects.get(id=client_id)
            client.delete()
            self.stdout.write(self.style.SUCCESS(f'Клиент с идентификатором: {client_id} удален.'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором: {client_id} не существует.'))

    def handle_get(self, **options):
        client_id = options['client_id']
        try:
            client = Client.objects.get(id=client_id)
            self.stdout.write(f"ID: {client.id}\n"
                              f"Имя: {client.name}\n"
                              f"Email: {client.email}\n"
                              f"Телефон: {client.phone}\n"
                              f"Адрес: {client.address}")
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором: {client_id} не существует.'))

# py manage.py client_crud create --name "Вася Пупки" --email "vasya@hacker.ru" --phone "+9156782354" --address "Moscows city"
# py manage.py client_crud update --client_id 1 --name "Обновленное Имя" --email "updated@email.com" --phone "8911233443" --address "Perm"
# py manage.py client_crud list
# py manage.py client_crud delete --client_id 1
# py manage.py client_crud get --client_id 1
