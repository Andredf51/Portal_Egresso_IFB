from django.urls import path
from . import views

from .views import CoordenadorView, TurmaView

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
    # path('turmas', views.exibir_turma, name='exibir_turma'),
    path('coordenador', CoordenadorView.as_view(), name='coordenador'),
    path('turmas', views.TurmaView.as_view(), name='exibir_turma'),
    path('egressos', views.EgressoView.as_view(), name='exibir_egresso'),
]