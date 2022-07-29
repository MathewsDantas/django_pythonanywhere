from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Simulado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    pont_total = models.DecimalField(max_digits=6,decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    data_fim = models.DateField('Data de encerramento', null=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Pontuacao: {self.pont_total} "

class Questao(models.Model):
    simulado = models.ForeignKey(Simulado,on_delete=models.CASCADE)
    texto = models.CharField(max_length= 200)
    pontuacao = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"Texto: {self.texto} - Pontuacao: {self.pontuacao} "

class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return f"Texto: {self.texto}"

