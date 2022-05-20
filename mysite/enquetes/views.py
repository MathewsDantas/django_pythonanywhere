from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

from enquetes.models import Pergunta

# Create your views here.
def index(request):
    quest_recent = Pergunta.objects.order_by('-data')[:5]
    context = {'quest_recent': quest_recent}
    return render(request, 'enquetes/index.html', context)

def detail(request, questao_id):
    try:
        pergunta = Pergunta.objects.get(pk = questao_id)
    except Pergunta.DoesNotExist:
        raise Http404("Questão não existe")
    return render(request, 'enquetes/details.html', {'pergunta':pergunta})

def results(request, questao_id):
    response = "Resultados da questão %s."
    return HttpResponse(response % questao_id)

def vote(request, questao_id):
    response = "Votação para a questão %s."
    return HttpResponse(response % questao_id)