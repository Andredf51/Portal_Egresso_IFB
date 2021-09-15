from django.urls import path
from django.views.generic.base import View
from usuarios.views import CriarCursoView, RegistrarUsuarioView

from . import views
from .views import CriarTurmaCreate

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('criarcurso/', CriarCursoView.as_view(), name='criarcurso'),
    path('criarturma/', CriarTurmaCreate.as_view(), name='criarturma'),

]