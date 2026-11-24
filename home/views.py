from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "<!doctype html><html lang='ru'><meta charset='utf-8'>"
        "<title>Django в Docker</title>"
        "<h1>Сайт Django работает!</h1>"
        "<p>Приложение запущено в Docker-контейнере.</p>"
    )
