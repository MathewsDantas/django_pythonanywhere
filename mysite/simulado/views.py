from django.http import HttpResponseRedirect
from django.shortcuts import render
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

def dashboard(request):
    meus_simulados = Simulado.objects.filter(usuario__user = request.user)
    return render(request, 'simulado/dashboard.html',{'simulados': meus_simulados})

def detalheSimulado(request, simulado_id):
    simulado = Simulado.objects.filter(pk= simulado_id)
    return render(request, 'simulado/detalheSimulado.html', {'simulado': simulado})

def resposta(request, simulado_id):
    simulado = Simulado.objects.filter(pk= simulado_id)
    return render(request, 'simulado/respostaSimulado.html', {'simulado': simulado})

class CriaSimulado(View):
    def get(self, request):
        return render(request, 'simulado/cadastroSimulado.html')

    def post(self, request):
        titulo = request.POST['titulo']
        pontuacao = request.POST.get('pontuacao')
        data_fim = request.POST['data_fim']
        texto_quest = request.POST['texto_quest']
        pont_quest = request.POST['pont_quest']
        alt01 = request.POST['alt01']
        alt02 = request.POST['alt02']

        if titulo and pontuacao and data_fim and texto_quest and pont_quest and alt01 and alt02:
            simulado = Simulado.objects.create(titulo = titulo, pont_total = pontuacao, data_fim = data_fim)
            questao = Questao.objects.create(texto= texto_quest, pontuacao= pont_quest, simulado= simulado)
            Resposta.objects.create(texto = alt01, questao = questao)
            Resposta.objects.create(texto = alt02, questao = questao)
            if request.POST['alt03']:
                    Resposta.objects.create(texto = request.POST['alt03'], questao = questao)
            if request.POST['alt04']:
                Resposta.objects.create(texto = request.POST['alt04'], questao = questao)

        return HttpResponseRedirect(reverse('simulado:simulados'))

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
            return HttpResponseRedirect(reverse('login'))
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
            login(user)
            return render(request, 'simulado/dashboard.html')
        else:
            erro = 'usuario e senha inválidas!'
            return HttpResponseRedirect(reverse('login'), {'erro': erro})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('simulados'))
