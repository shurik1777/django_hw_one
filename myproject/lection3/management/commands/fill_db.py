from random import choices

from django.core.management.base import BaseCommand
from ...models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem, blanditiis debitis eius eum minima nostrum" \
         " odio optio sapiente tenetur voluptas.Lorem ipsum dolor sit amet, consectetur adipisicin" \
    "Lorem ipsum dolor sit amet, consectetur adipisicin Lorem ipsum dolor sit amet, consectetur adipisicin" \
    "Lorem ipsum dolor sit amet, consectetur adipisicin Lorem ipsum dolor sit amet, consectetur adipisicin " \
    "Lorem ipsum dolor sit amet, consectetur adipisicin" \
    "Lorem ipsum dolor sit amet, consectetur adipisicin Lorem ipsum dolor sit amet, consectetur adipisicin"


class Command(BaseCommand):
    help = 'Создание ложных авторов и постов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@gmail.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author,
                )
                post.save()
