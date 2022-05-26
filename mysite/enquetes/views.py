from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from enquetes.models import Pergunta
from enquetes.models import Alternativa

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
    pergunta = get_object_or_404(Pergunta, pk = questao_id)
    return render(request, 'enquetes/results.html',{'pergunta':pergunta})

def vote(request, questao_id):
    pergunta = get_object_or_404(Pergunta, pk = questao_id)
    try:
        selected_alternativa = pergunta.alternativa_set.get(pk = request.POST['alternativa'])
    except (KeyError, Alternativa.DoesNotExist):
        return render(request, 'enquetes/details.html', {'pergunta':pergunta,'error_message':"Você não selecionou uma opção"})
    else:
        selected_alternativa.voto+=1
        selected_alternativa.save()    
        return HttpResponseRedirect(reverse('enquetes:results',
            args=(questao_id,)))