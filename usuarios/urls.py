from django.urls import path
from usuarios.views import CreateUsuarioView, CreateCursosView, DeleteCursoView, DeleteTurmaView, DeleteAlunoView

from .views import CreateTurmaView, GerenciarCursosView, UpdateCursoView, GerenciarTurmaView, UpdateTurmaView, GerenciarAlunosView

urlpatterns = [
    path('gerenciaraluno/', GerenciarAlunosView.as_view(), name='gerenciaraluno'),
    path('registrar/', CreateUsuarioView.as_view(), name='registrar'),
    path('<int:pk>/deletea/', DeleteAlunoView.as_view(), name='del_aluno'),
    path('gerenciarturma/', GerenciarTurmaView.as_view(), name='gerenciarturma'),
    path('criarturma/', CreateTurmaView.as_view(), name='criarturma'),
    path('<int:pk>/updatet/', UpdateTurmaView.as_view(), name='upd_turma'),
    path('<int:pk>/deletet/', DeleteTurmaView.as_view(), name='del_turma'),
    path('criarcurso/', CreateCursosView.as_view(), name='criarcurso'),
    path('gerenciarcurso/', GerenciarCursosView.as_view(), name='gerenciarcurso'),
    path('<int:pk>/updatec/', UpdateCursoView.as_view(), name='upd_curso'),
    path('<int:pk>/deletec/', DeleteCursoView.as_view(), name='del_curso'),

]