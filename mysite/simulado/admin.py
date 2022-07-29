from django.contrib import admin
from simulado.models import Usuario, Questao, Resposta, Simulado
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Simulado)
admin.site.register(Questao)
admin.site.register(Resposta)