from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from .models import Simulado, Questao, Resposta, Usuario


#visualização de simulados específicos, com a opção de submeter;
#visualização do resultado da resposta de um simulado, apresentando as respostas corretas, respostas erradas e a soma das pontuações.

class Simulados(View):
    def get(self, request):
        simulados = Simulado.objects.all()
        contexto = {'simulados':simulados}
        return render(request, 'simulado/simulados.html',contexto)

@login_required(login_url="/simulado/login/")
def dashboard(request):
    meus_simulados = Simulado.objects.filter(usuario = request.user)
    return render(request, 'simulado/dashboard.html',{'simulados': meus_simulados})

def detalheSimulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, pk=simulado_id)
    questoes = Questao.objects.filter(simulado = simulado)

    return render(request, 'simulado/detalheSimulado.html', {'simulado': simulado, 'questoes': questoes})


class resposta(View):
    def post(self, request, simulado_id):
        simulado = get_object_or_404(Simulado, pk=simulado_id)
        questoes = Questao.objects.filter(simulado= simulado)
        lista_respostas = []
        nota = 0
        for q in questoes:
            alternativa = r"alternativa%s"%q.id
            id_alt = request.POST.get(alternativa)
            resposta = get_object_or_404(Resposta, pk= id_alt)
            if resposta.correta:
                nota+= q.pontuacao  
            lista_respostas.append(resposta)
        
        return render(request, 'simulado/respostaSimulado.html', {'simulado': simulado,'respostas': lista_respostas, 'nota': nota})

@method_decorator(login_required(login_url="/simulado/login/"), name='dispatch')
class CriaSimulado(View):
    def get(self, request):
        return render(request, 'simulado/cadastroSimulado.html')

    def post(self, request):
        titulo = request.POST['titulo']
        pontuacao = request.POST.get('pontuacao')
        data_fim = request.POST['data_fim']
        texto_quest = request.POST['texto_quest']
        alt01 = request.POST['alt01']
        alt02 = request.POST['alt02']

        if titulo and pontuacao and texto_quest and alt01 and alt02:
            simulado = Simulado.objects.create(usuario= request.user, titulo= titulo, pont_total= pontuacao, data_fim = data_fim, qtd_questoes = 0)
            questao = Questao.objects.create(texto= texto_quest, simulado= simulado)
            correta = request.POST['correta']
            
            resposta = Resposta.objects.create(texto = alt01, questao = questao)
            if correta == 'alt01':
                resposta.correta = True
                resposta.save()

            resposta = Resposta.objects.create(texto = alt02, questao = questao)
            if correta == 'alt02':
                resposta.correta = True
                resposta.save()

            if request.POST['alt03']:
                resposta = Resposta.objects.create(texto = request.POST['alt03'], questao = questao)
                if correta == 'alt03':
                    resposta.correta = True
                    resposta.save()

            if request.POST['alt04']:
                resposta = Resposta.objects.create(texto = request.POST['alt04'], questao = questao)
                if correta == 'alt04':
                    resposta.correta = True
                    resposta.save()
            simulado.qtd_questoes +=1
            simulado.save()
            pont_simulado = simulado.pont_total
            qtd_quest = simulado.qtd_questoes
            pont_quest = int(pont_simulado)/qtd_quest
            questoes = Questao.objects.filter(simulado = simulado)
            for quest in questoes:
                quest.pontuacao = pont_quest
                quest.save()
        
        return HttpResponseRedirect(reverse('simulado:dashboard'))

@method_decorator(login_required(login_url="/simulado/login/"), name='dispatch')
class CriaQuestao(View):
    def get(self, request, simulado_id):
        simulado = get_object_or_404(Simulado, pk=simulado_id)
        return render(request, 'simulado/cadastroQuestao.html', {'simulado': simulado})
    def post(self, request, simulado_id):
        texto_quest = request.POST['texto_quest']
        alt01 = request.POST['alt01']
        alt02 = request.POST['alt02']

        if texto_quest and alt01 and alt02:
            simulado = get_object_or_404(Simulado, pk = simulado_id)
            questao = Questao.objects.create(texto= texto_quest, simulado= simulado) 
            correta = request.POST['correta']
            
            resposta = Resposta.objects.create(texto = alt01, questao = questao)
            if correta == 'alt01':
                resposta.correta = True
                resposta.save()

            resposta = Resposta.objects.create(texto = alt02, questao = questao)
            if correta == 'alt02':
                resposta.correta = True
                resposta.save()

            if request.POST['alt03']:
                resposta = Resposta.objects.create(texto = request.POST['alt03'], questao = questao)
                if correta == 'alt03':
                    resposta.correta = True
                    resposta.save()

            if request.POST['alt04']:
                resposta = Resposta.objects.create(texto = request.POST['alt04'], questao = questao)
                if correta == 'alt04':
                    resposta.correta = True
                    resposta.save()
            # divide a pontuação de acordo com a qtd de questões no simulado.
            simulado.qtd_questoes +=1
            simulado.save()
            pont_simulado = simulado.pont_total
            qtd_quest = simulado.qtd_questoes
            pont_quest = int(pont_simulado)/qtd_quest
            questoes = Questao.objects.filter(simulado = simulado)
            for quest in questoes:
                quest.pontuacao = pont_quest
                quest.save()

        return HttpResponseRedirect(reverse( 'simulado:detalhe', args=(simulado_id,)))


class CadastroUsuario(View):
    def get(self, request):
        return render(request, 'simulado/cadastroUsuario.html')
    def post(self, request):
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        if nome and email and senha:
            user = User.objects.create_user(
                username=nome, password=senha, email=email)
            Usuario.objects.create(user=user)
            return HttpResponseRedirect(reverse('simulado:login'))
        else:
            erro = 'Informe corretamente os parâmetros necessários!'

            return render(request, 'simulado/cadastroUsuario.html', {'erro': erro})

class LoginView(View):
    def get(self, request):
        return render(request, 'simulado/login.html')
    def post(self, request):
        username = request.POST.get('username')
        senha =  request.POST.get('senha')
        user = authenticate(username = username, password = senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('simulado:dashboard'))
        else:
            erro = 'usuario e senha inválidas!'
            return HttpResponseRedirect(reverse('simulado:login'), {'erro': erro})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('simulado:simulados'))
