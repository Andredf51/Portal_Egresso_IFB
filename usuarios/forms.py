from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import related

#Os atributos das classes são os mesmo do formulário (atributo nome)

class RegistrarUsuarioForm(forms.Form):
    email = forms.EmailField(required=True)
    nome = forms.CharField(required=True)
    foto = forms.CharField(required=True)
    cargo = forms.CharField(required=True)
    empresa = forms.CharField(required=True)
    rede = forms.CharField(required=True)
    lattes = forms.CharField(required=True)
    interesses = forms.CharField(required=True)
    relato = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class CriarCursoForm(forms.Form):
    nome = forms.CharField(required=True)
    nivel = forms.CharField(required=True)
    campus= forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(CriarCursoForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Curso já existente'+self.nome)
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class CriarTurmaForm(forms.Form):
    periodo = forms.CharField(required=True)
    data= forms.CharField(required=True)
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