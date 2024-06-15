from django.core.management.base import BaseCommand
from myproject.wmodel.models import Article
from django.utils import timezone


class Command(BaseCommand):
    help = 'Manage articles'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='subcommand')

        parser_create = subparsers.add_parser('create', help='Создать новый продукт')
        parser_create.add_argument('--title', type=str, help='Название продукта')
        parser_create.add_argument('--content', type=str, help='Описание продукта')
        parser_create.add_argument('--price', type=float, help='Цена продукта')
        parser_create.add_argument('--amount', type=float, help='Сумма продукта')
        parser_create.add_argument('--date', type=str, help='Дата поступления продукта',
                                   default=timezone.now().strftime("%Y-%m-%d"))

        parser_update = subparsers.add_parser('update', help='Обновить существующий продукт')
        parser_update.add_argument('--article_id', type=int, help='Идентификатор продукта для обновления')
        parser_update.add_argument('--title', type=str, help='Название нового продукта')
        parser_update.add_argument('--content', type=str, help='Содержание нового продукта')
        parser_update.add_argument('--price', type=float, help='Цена нового продукта')
        parser_update.add_argument('--amount', type=float, help='Количество нового продукта')
        parser_update.add_argument('--date', type=str, help='Дата поступления нового продукта')

        parser_list = subparsers.add_parser('list', help='Перечислить все продукты')

        parser_delete = subparsers.add_parser('delete', help='Удалить продукт')
        parser_delete.add_argument('--article_id', type=int, help='Идентификатор продукта, который нужно удалить')
        parser_get = subparsers.add_parser('get', help='Получить информацию о товаре по id')
        parser_get.add_argument('--article_id', type=int, help='Идентификатор товара для получения информации')

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
        article = Article(
            title=options['title'],
            content=options['content'],
            price=options['price'],
            amount=options['amount'],
            date=options['date'] or timezone.now().strftime("%Y-%m-%d")
        )
        article.save()
        self.stdout.write(self.style.SUCCESS('Продукт успешно создан'))

    def handle_update(self, **options):
        article_id = options['article_id']
        title = options['title']
        content = options['content']
        price = options['price']
        amount = options['amount']
        date = options['date'] or timezone.now().strftime("%Y-%m-%d")

        article = Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.price = price
        article.amount = amount
        article.date = date
        article.save()
        self.stdout.write(self.style.SUCCESS('Продукт успешно обновлен'))

    def handle_list(self):
        articles = Article.objects.all()
        for article in articles:
            print(f"{article.id}: {article.title}, {article.price}")

    def handle_delete(self, **options):
        article_id = options['article_id']
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            self.stdout.write(self.style.SUCCESS(f'Заказ с идентификатором: {article_id} удален.'))
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Заказ с идентификатором: {article_id} не существует.'))

    def handle_get(self, **options):
        product_id = options['article_id']
        try:
            product = Article.objects.get(id=product_id)
            self.stdout.write(f"ID: {product.id}\n"
                              f"Название: {product.title}\n"
                              f"Описание товара: {product.content}\n"
                              f"Цена: {product.price}\n"
                              f"Количество на складе: {product.amount}\n"
                              f"Дата добавления на складе: {product.date}")
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с идентификатором: {product_id} не существует.'))

# py manage.py article_crud create --title "Gbysda" --content "adasdadahacker.ru" --price 2 --amount 5
# py manage.py article_crud update --article_id 1 --title "Обновленное Имя" --content "updated@email.com"
# py manage.py article_crud list
# py manage.py article_crud delete --article_id 1
# py manage.py article_crud get --article_id 1
