from django.urls import path
from . import views

from .views import CoordenadorView, IndexView, TurmaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
    path('coordenador', CoordenadorView.as_view(), name='coordenador'),
    path('turmas', views.TurmaView.as_view(), name='exibir_turma'),
    path('egressos', views.EgressoView.as_view(), name='exibir_egresso'),

]