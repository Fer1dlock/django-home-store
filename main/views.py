from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context=context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему именно мы, и как мы работаем',
    }

    return render(request, 'main/about.html', context=context)
