from django.shortcuts import render
from django.views import generic
from perfis.models import Alunos, Curso, Turma

from django.views.generic import TemplateView

# novas importações, pode ser as únicas
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic import TemplateView

# Autenticando com Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Autentificação por grupos de usuários
from braces.views import GroupRequiredMixin


class IndexView(ListView):
    models = Curso
    template_name = 'index.html'
    queryset = Curso.objects.filter(nivel='Superior')
    context_object_name = 'texto'


def listacursosview(request, curso_id):
    indexcursos = Curso.objects.filter(nivel=curso_id)
    return render(request, 'listacursos.html', { "indexcursos" : indexcursos})

# class IndexView(ListView):
#     models = Curso
#     template_name = 'index.html'
#     queryset = Curso.objects.filter(nivel='Superior')
#     context_object_name = 'perfis'


def exibir(request, perfil_id):

    alunos = Alunos.objects.get(id=perfil_id)
    return render(request, 'alunos.html', { "alunos" : alunos})


# rota protegida, somente com login, somente grupo Coordenador
class CoordenadorView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenador"
    template_name = 'pcoordenador.html'


# rota protegida, somente com login, somente grupo egresso
class EgressoupdView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login_aluno')
    group_required = u"Egresso"
    template_name = 'pegresso_gerenciar.html'


def listarturmasview(request, turma_id):
    turmas2 = Turma.objects.filter(curso=turma_id)
    return render(request, 'turma.html', { "turmas2" : turmas2})


def listaregressoview(request, egresso_id):
    egressos1 = Alunos.objects.filter(turmaa__id=egresso_id)

    return render(request, 'pegresso.html', { "egressos1" : egressos1})


#passos para criar uma aplicação
#1° View - importa o TemplateView
#2° criar a class
#3° URL

# def listarturmasview(request, turma_id):
#     turmas2 = Turma.objects.filter(curso=turma_id)
#     return render(request, 'turma.html', { "turmas2" : turmas2})

# class TurmaView(generic.ListView):
#     template_name = 'turma.html'
#     model = Turma
#     queryset = Turma.objects.all()
#     context_object_name = 'turmas'

# class EgressoView(generic.ListView):
#     template_name = 'pegresso.html'
#     model = Alunos
#     queryset = Alunos.objects.all()
#     context_object_name = 'egressos'