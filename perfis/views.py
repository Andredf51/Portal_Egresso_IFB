from django.shortcuts import render
from django.views import generic
from perfis.models import Alunos, Curso, Turma

from django.views.generic import TemplateView

# novas importações, pode ser as únicas
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

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


class CoordenadorView(TemplateView):
    template_name = 'pcoordenador.html'


class TurmaView(generic.ListView):
    template_name = 'turma.html'
    model = Turma
    queryset = Turma.objects.all()
    context_object_name = 'turmas'


class EgressoView(generic.ListView):
    template_name = 'pegresso.html'
    model = Alunos
    queryset = Alunos.objects.all()
    context_object_name = 'egressos'



#passos para criar uma aplicação
#1° View - importa o TemplateView
#2° criar a class
#3° URL