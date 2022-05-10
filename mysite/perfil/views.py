from django.shortcuts import render
from django.http import HttpResponse

def perfil(request):
    html = "<html><body>Nome: Mathews Dantas Bezerra dos Santos.<br>Matricula: 20211014040007</body></html>"
    return HttpResponse(html)
