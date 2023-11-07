from django.http import HttpResponse
from django.shortcuts import render

# Criar endpoint para leitura de arquivos xlsx


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
