from django import forms
from perfis.models import Alunos, Curso, Turma

# Importações necessárias para formulário de usuários
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Os atributos das classes são os mesmo do formulário (atributo nome)

class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    nome = forms.CharField(max_length=150)
    curso = forms.CharField(max_length=100)
    foto = forms.CharField(max_length=100)
    cargo = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    rede = forms.CharField(max_length=50)
    lattes = forms.CharField(max_length=100)
    interesses = forms.CharField(max_length=100)
    relato = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'nome', 'curso', 'foto', 'cargo', 'empresa', 'rede', 'lattes', 'interesses', 'relato', 'password1', 'password2']


# Formulário para coordenador
class CoordenadorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    nome_completo = forms.CharField(max_length=100)
    curso = forms.CharField(max_length=100)
    telefone = forms.IntegerField(max_value=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'nome_completo', 'curso', 'telefone', 'password1', 'password2']


class CriarTurmaForm(forms.Form):
    periodo = forms.CharField(required=True)
    data = forms.CharField(required=True)
    foto = forms.CharField(required=True)
    curso = forms.CharField(required=True)
    alunos = forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(CriarTurmaForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['periodo']).exists()

        if user_exists:
            self.adiciona_erro('Turma já existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class CursoModelForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'


# Código original para criar aluno
# class RegistrarUsuarioForm(forms.Form):
#     email = forms.EmailField(required=True)
#     nome = forms.CharField(required=True)
#     foto = forms.CharField(required=True)
#     cargo = forms.CharField(required=True)
#     empresa = forms.CharField(required=True)
#     rede = forms.CharField(required=True)
#     lattes = forms.CharField(required=True)
#     interesses = forms.CharField(required=True)
#     relato = forms.CharField(required=True)
#
#     def is_valid(self):
#         valid = True
#         if not super(RegistrarUsuarioForm, self).is_valid():
#             self.adiciona_erro('Por favor, verifique os dados informados')
#             valid = False
#
#         user_exists = User.objects.filter(username=self.data['nome']).exists()
#
#         if user_exists:
#             self.adiciona_erro('Usuario ja existente')
#             valid = False
#
#         return valid
#
#     def adiciona_erro(self, message):
#         errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
#         errors.append(message)
