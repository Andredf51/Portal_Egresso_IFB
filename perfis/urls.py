from django.urls import path
from . import views

from .views import CoordenadorView, EgressoupdView, IndexView, listacursosview

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('lista2/<str:curso_id>', views.listacursosview, name='lista2'),
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
    path('coordenador', CoordenadorView.as_view(), name='coordenador'),
    path('turmas/<str:turma_id>', views.listarturmasview, name='exibir_turma2'),
    path('egresso', EgressoupdView.as_view(), name='egresso'),

    path('egressos/<str:egresso_id>', views.listaregressoview, name='exibir_egresso'),

]

# urls originas class
#    path('turmas', views.TurmaView.as_view(), name='exibir_turma'),
# path('turmas/<str:turma_id>', views.listarturmasview, name='exibir_turma2'),

# path('egressos', views.EgressoView.as_view(), name='exibir_egresso'),