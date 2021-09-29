from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Alunos, Curso, Turma

from django.views.generic import FormView

# teste de create
from django.urls import reverse_lazy

# Novo formato resumido
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RegistrarUsuarioForm, CriarTurmaForm, CursoModelForm


class GerenciarAlunosView(ListView):
    models = Alunos
    template_name = 'gerenciar_alunos.html'
    queryset = Alunos.objects.all()
    context_object_name = 'listaralunos'


class CreateUsuarioView(View):
    model = Alunos
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # preenche o from
        form = RegistrarUsuarioForm(request.POST)

        # verifica se é valido
        if form.is_valid():
            dados_form = form.data

            # cria o usuario
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            # cria o perfil
            alunos = Alunos(nome=dados_form['nome'],
                            foto=dados_form['foto'],
                            cargo_atual=dados_form['cargo'],
                            empresa_atual=dados_form['empresa'],
                            rede_social=dados_form['rede'],
                            lattes=dados_form['lattes'],
                            interesses=dados_form['interesses'],
                            relato_pessoal=dados_form['relato'],

                            usuario=usuario)

            # grava no banco
            alunos.save()

            # redireciona para index
            return redirect('index')

        # so chega aqui se nao for valido
        # vamos devolver o form para mostrar o formulario preenchido
        return render(request, self.template_name, {'form': form})


class DeleteAlunoView(DeleteView):
    model = Alunos
    template_name = 'del_aluno.html'
    success_url = reverse_lazy('gerenciaraluno')


class GerenciarCursosView(ListView):
    models = Curso
    template_name = 'gerenciar_cursos.html'
    queryset = Curso.objects.all()
    context_object_name = 'listarcursos'


class CreateCursosView(CreateView):
    model = Curso
    template_name = 'criarcurso.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('gerenciarcurso')


class UpdateCursoView(UpdateView):
    model = Curso
    template_name = 'criarcurso.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('gerenciarcurso')


class DeleteCursoView(DeleteView):
    model = Curso
    template_name = 'del_curso.html'
    success_url = reverse_lazy('gerenciarcurso')


class GerenciarTurmaView(ListView):
    models = Turma
    template_name = 'gerenciar_turma.html'
    queryset = Turma.objects.all()
    context_object_name = 'listarturmas'


class CreateTurmaView(CreateView):
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso', 'alunos']
    template_name = 'criarturma.html'
    success_url = reverse_lazy('gerenciarturma')


class UpdateTurmaView(UpdateView):
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso', 'alunos']
    template_name = 'criarturma.html'
    success_url = reverse_lazy('gerenciarturma')


class DeleteTurmaView(DeleteView):
    model = Turma
    template_name = 'del_turma.html'
    success_url = reverse_lazy('gerenciarturma')




