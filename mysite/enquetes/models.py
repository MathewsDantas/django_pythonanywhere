from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(
        max_length=200)

    data = models.DateTimeField('Data de publicação')

    def __str__(self):
        return f"{self.texto} - {self.data}"

class Alternativa(models.Model):
    pergunta = models.ForeignKey(
        Pergunta,on_delete=models.CASCADE) 

    voto = models.IntegerField(default=0)

    texto = models.CharField(
        max_length=200
    )    

    def __str__(self):
        return f"{self.pergunta.texto} - {self.texto}"
