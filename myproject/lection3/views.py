from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse("Hello World from Django")


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello World from Django")


def year_post(request, year):
    text = ""
    ...
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ...
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создает списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумаля на тем, "
                   "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "lection3/index.html", context)


class TemplIf(TemplateView):
    template_name = "my_template.html"