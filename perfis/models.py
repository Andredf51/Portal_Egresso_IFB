from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alunos(models.Model):

    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255, null=False)
    cargo_atual = models.CharField(max_length=255, null=False)
    empresa_atual = models.CharField(max_length=255, null=False)
    rede_social = models.CharField(max_length=255, null=False)
    lattes = models.CharField(max_length=255, null=False)
    interesses = models.CharField(max_length=255, null=False)
    relato_pessoal = models.CharField(max_length=255, null=False)

    contatos = models.ManyToManyField('self')

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alunos")

    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome


class Curso(models.Model):

    nome = models.CharField(max_length=255, null=False)
    nivel = models.CharField(max_length=255, null=False)
    campus = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome


class Turma(models.Model):

    periodo = models.CharField(max_length=255, null=False)
    data_formatura = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Alunos)

    def __str__(self):
        return self.periodo