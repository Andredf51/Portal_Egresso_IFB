from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Alunos, Curso, Turma
from usuarios.forms import RegistrarUsuarioForm, CriarCursoForm

from django.views.generic import FormView

# teste de create
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class RegistrarUsuarioView(View):
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


class CriarCursoView(View):
    template_name = 'criarcurso.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # preenche o from
        form = CriarCursoForm(request.POST)

        # verifica se é valido
        if form.is_valid():
            dados_form = form.data

            # cria o perfil
            cursos = Curso(nome=dados_form['nome'],
                           nivel=dados_form['nivel'],
                           campus=dados_form['campus'],

                           )

            # grava no banco
            cursos.save()

            # redireciona para index
            return redirect('index')

        # so chega aqui se nao for valido
        # vamos devolver o form para mostrar o formulario preenchido
        return render(request, self.template_name, {'form': form})


class CriarTurmaCreate(CreateView):
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso', 'alunos']
    template_name = 'criarturma.html'
    success_url = reverse_lazy('index')
