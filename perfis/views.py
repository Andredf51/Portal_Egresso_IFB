from django.shortcuts import render
from django.views import generic
from perfis.models import Alunos, Curso, Turma

from django.views.generic import TemplateView

# Create your views here.

def index(request):
    superior = Curso.objects.get(id=1)
    tecnico = Curso.objects.all()
    return render(request, 'index.html', {'perfis' : tecnico})

def exibir(request, perfil_id):

    alunos = Alunos.objects.get(id=perfil_id)
    return render(request, 'alunos.html', { "alunos" : alunos})


def exibir_turma(request):
    turma = Turma.objects.get(id=2)
    return render(request, 'turma.html', {"turma" : turma})


class CoordenadorView(TemplateView):
    template_name = 'pcoordenador.html'


class TurmaView(generic.ListView):
    template_name = 'turma.html'
    model = Turma
    queryset = Turma.objects.filter(id=2)
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