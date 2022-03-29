from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alunos(models.Model):
    TrabalhaArea_CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
        ('EmParte', 'Em parte'),
    )
    CursoExtra_CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )

    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    foto = models.CharField(max_length=150)
    cargo_atual = models.CharField(max_length=50)
    empresa_atual = models.CharField(max_length=50)
    trabalha_area = models.CharField(max_length=8, choices=TrabalhaArea_CHOICES)
    ifb_ajudou = models.CharField(max_length=8, choices=TrabalhaArea_CHOICES)
    grade_ifb = models.CharField(max_length=10)
    curso_extra = models.CharField(max_length=10, choices=CursoExtra_CHOICES)
    qual_curso_extra = models.CharField(max_length=30)
    opiniao_curso_ifb = models.CharField(max_length=100)
    pode_melhorar = models.CharField(max_length=100)
    rede_social = models.CharField(max_length=100)
    lattes = models.CharField(max_length=100)
    validado = models.CharField(max_length=5)


    contatos = models.ManyToManyField('self')

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alunos")

    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL_CHOICES = (
        ('Superior', 'Superior (Bacharelado / Licenciatura)'),
        ('Superior', 'Superior (Tecnologia)'),
        ('Tecnico', 'Técnico (Integrado)'),
        ('Tecnico', 'Técnico(Subsequente)'),
    )

    nome = models.CharField(max_length=255, null=False)
    nivel = models.CharField(max_length=255, choices=NIVEL_CHOICES, null=False)
    campus = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome


class Turma(models.Model):

    periodo = models.CharField(max_length=255, null=False)
    data_formatura = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Alunos, related_name='turmaa')

    def __str__(self):
        return self.periodo