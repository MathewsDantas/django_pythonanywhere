from xml.etree.ElementInclude import include
from django.urls import path
from mysite.perfil.views import perfil

urlpatterns = [
    path('index/',perfil),
]
