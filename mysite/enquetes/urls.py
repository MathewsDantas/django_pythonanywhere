from django.urls import path
from enquetes.views import index,detail,results,vote

urlpatterns = [
    path('',index, name='index'),

    path('<int:questao_id>/', detail, name='detail'),

    path('<int:questao_id>/results/', results, name='results'),

    path('<int:questao_id>/vote/', vote, name= 'vote'),

]