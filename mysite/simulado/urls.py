from django.urls import path
from . import views

app_name = 'simulado'
urlpatterns = [

    path('', views.Simulados.as_view(),
        name='simulados'),
    path('dashboard/', views.dashboard, 
        name='dashboard'),
    path('simulado/<int:simulado_id>/', views.detalheSimulado, 
        name='detalhe'),
    path('simulado/resposta/<int:simulado_id>/', views.detalheSimulado, 
        name='resposta'),

    path('cadastrosimulado/', views.CriaSimulado.as_view(), 
        name= 'criasimulado'),
    path('cadastrousuario/', views.CadastroUsuario.as_view(), 
        name= 'cadastrousuario'),

    path('login/', views.LoginView.as_view(), 
        name= 'login'),
    path('logout/', views.logoutView, 
        name='logout'),

]