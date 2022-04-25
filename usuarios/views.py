from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import View
from perfis.models import Alunos, Curso, Turma

from django.views.generic import FormView

# Novo formato resumido
from django.views.generic import ListView

# Criação de usuários e CRUD(Novo)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from .forms import CoordenadorForm, RegistrarUsuarioForm, CriarTurmaForm, CursoModelForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import PerfilCoordenador

# Autenticando com Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Autentificação por grupos de usuários
from braces.views import GroupRequiredMixin


################# Alunos ###############################
class GerenciarAlunosView(ListView):
    models = Alunos
    template_name = 'gerenciar_alunos.html'
    queryset = Alunos.objects.all()
    context_object_name = 'listaralunos'


# Teste de uso da CreateView
class CreateUsuario(CreateView):
    template_name = 'registrar.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy('login_aluno')

    # metodo para submeter formulários
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Egresso')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Alunos.objects.create(usuario=self.object)

        return url


class AlunoUpdate(UpdateView):
    template_name = 'registrar.html'
    model = Alunos
    fields = ['nome', 'curso', 'cargo_atual', 'empresa_atual', 'trabalha_area', 'ifb_ajudou', 'grade_ifb', 'curso_extra',
              'qual_curso_extra', 'opiniao_curso_ifb', 'pode_melhorar', 'rede_social', 'lattes']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Alunos, usuario=self.request.user)
        return self.object


# Update do Egresso na página do coordenador (teste)
class UpdateEgressoView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Alunos
    template_name = 'registrar.html'
    fields = ['nome', 'curso', 'validado']
    success_url = reverse_lazy('index')

# Delete da página do coordenado, aqui o coordenar apaga o aluno
class DeleteAlunoView(DeleteView):
    model = Alunos
    template_name = 'del_aluno.html'
    success_url = reverse_lazy('gerenciaraluno')


# Delete da página do egresso
class DeleteAlunoEgresso(DeleteView):
    model = Alunos
    template_name = 'del_aluno.html'
    success_url = reverse_lazy('gerenciaraluno')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Alunos, usuario=self.request.user)
        return self.object


################# Coordenador ###############################
class CoodenadorCreate(CreateView):
    template_name = 'criar_coordenador.html'
    form_class = CoordenadorForm
    success_url = reverse_lazy('login')

    # metodo para submeter formulários
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='EmAnalise')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        PerfilCoordenador.objects.create(usuario=self.object)

        return url


class CoordenadorUpdate(UpdateView):
    template_name = 'criar_coordenador.html'
    model = PerfilCoordenador
    fields = ['nome_completo', 'curso', 'telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilCoordenador, usuario=self.request.user)
        return self.object


class DeleteCoordenador(DeleteView):
    model = PerfilCoordenador
    template_name = 'del_coordenador.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilCoordenador, usuario=self.request.user)
        return self.object


################# Cursos ###############################
class GerenciarCursosView(ListView):
    models = Curso
    template_name = 'gerenciar_cursos.html'
    queryset = Curso.objects.all()
    context_object_name = 'listarcursos'


class CreateCursosView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Curso
    template_name = 'criarcurso.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('gerenciarcurso')


class UpdateCursoView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Curso
    template_name = 'criarcurso.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('gerenciarcurso')


class DeleteCursoView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Curso
    template_name = 'del_curso.html'
    success_url = reverse_lazy('gerenciarcurso')


################# Turmas ###############################
class GerenciarTurmaView(ListView):
    models = Turma
    template_name = 'gerenciar_turma.html'
    queryset = Turma.objects.all()
    context_object_name = 'listarturmas'


class CreateTurmaView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso', 'alunos']
    template_name = 'criarturma.html'
    success_url = reverse_lazy('gerenciarturma')


class UpdateTurmaView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso', 'alunos']
    template_name = 'criarturma.html'
    success_url = reverse_lazy('gerenciarturma')


class DeleteTurmaView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    model = Turma
    template_name = 'del_turma.html'
    success_url = reverse_lazy('gerenciarturma')


# Código origina usuário
# class CreateUsuarioView(View):
#     model = Alunos
#     template_name = 'registrar.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         # preenche o from
#         form = RegistrarUsuarioForm(request.POST)
#
#         # verifica se é valido
#         if form.is_valid():
#             dados_form = form.data
#
#             # cria o usuario
#             usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
#
#             # cria o perfil
#             alunos = Alunos(nome=dados_form['nome'],
#                             foto=dados_form['foto'],
#                             cargo_atual=dados_form['cargo'],
#                             empresa_atual=dados_form['empresa'],
#                             rede_social=dados_form['rede'],
#                             lattes=dados_form['lattes'],
#                             interesses=dados_form['interesses'],
#                             relato_pessoal=dados_form['relato'],
#
#                             usuario=usuario)
#
#             # grava no banco
#             alunos.save()
#
#             # redireciona para index
#             return redirect('index')
#
#         # so chega aqui se nao for valido
#         # vamos devolver o form para mostrar o formulario preenchido
#         return render(request, self.template_name, {'form': form})



