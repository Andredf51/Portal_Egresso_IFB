from django.shortcuts import render
from django.views.generic.base import View
from perfis.models import Alunos, Curso, Turma

from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html', { 'perfis' : Curso.objects.all()})

def exibir(request, perfil_id):

    alunos = Alunos.objects.get(id=perfil_id)
    return render(request, 'alunos.html', { "alunos" : alunos})


def exibir_turma(request):
    turma = Turma.objects.get(id=2)
    return render(request, 'turma.html', {"turma" : turma})


class CoordenadorView(TemplateView):
    template_name = 'pcoordenador.html'

class TurmaView(TemplateView):
    template_name = 'turma.html'

#passos para criar uma aplicação
#1° View - importa o TemplateView
#2° criar a class
#3° URL