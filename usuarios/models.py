from django.db import models
from django.contrib.auth.models import User


# Criar um perfil personalizado para usuários
class PerfilCoordenador(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    curso = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=12, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
