from django.urls import path
from usuarios.views import CreateUsuario, CreateCursosView, DeleteCursoView, DeleteTurmaView, DeleteAlunoView

# Usar para autentificações
from django.contrib.auth import views as auth_views

from .views import CreateTurmaView, GerenciarCursosView, UpdateCursoView, GerenciarTurmaView, UpdateTurmaView, \
    GerenciarAlunosView, CoodenadorCreate, CoordenadorUpdate, AlunoUpdate, DeleteCoordenador, DeleteAlunoEgresso

urlpatterns = [
    # Criar usuários
    path('gerenciaraluno/', GerenciarAlunosView.as_view(), name='gerenciaraluno'),
    path('registrar/', CreateUsuario.as_view(), name='registrar'),
    path('<int:pk>/deletea/', DeleteAlunoView.as_view(), name='del_aluno'),
    path('updatealuno/', AlunoUpdate.as_view(), name='upd_aluno2'),
    path('<int:pk>/updatea/', AlunoUpdate.as_view(), name='upd_aluno'),
    path('deletealuno/', DeleteAlunoEgresso.as_view(), name='del_aluno2'),
    path('criarcoordenador/', CoodenadorCreate.as_view(), name='criar_coordenador'),
    path('updatecoordenador/', CoordenadorUpdate.as_view(), name='upd_coordenador'),
    path('deletecoordenador/', DeleteCoordenador.as_view(), name='del_coordenador'),

    # Gerenciar Turma
    path('gerenciarturma/', GerenciarTurmaView.as_view(), name='gerenciarturma'),
    path('criarturma/', CreateTurmaView.as_view(), name='criarturma'),
    path('<int:pk>/updatet/', UpdateTurmaView.as_view(), name='upd_turma'),
    path('<int:pk>/deletet/', DeleteTurmaView.as_view(), name='del_turma'),

    # Gerenciar Cursos
    path('criarcurso/', CreateCursosView.as_view(), name='criarcurso'),
    path('gerenciarcurso/', GerenciarCursosView.as_view(), name='gerenciarcurso'),
    path('<int:pk>/updatec/', UpdateCursoView.as_view(), name='upd_curso'),
    path('<int:pk>/deletec/', DeleteCursoView.as_view(), name='del_curso'),

    # Autentificação de usuários
    path('login/', auth_views.LoginView.as_view(template_name='login_autentificado.html'), name='login'),
    path('loginaluno/', auth_views.LoginView.as_view(template_name='login_aluno.html'), name='login_aluno'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Usar para autentificações - Código original
# path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')