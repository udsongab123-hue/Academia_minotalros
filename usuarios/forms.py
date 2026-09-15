from typing import Any

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from usuarios.models import Aluno


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        labels = {
            'username':'Usuário',
            'email':'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'estado',
            'sexo',
            'nascimento',
            'celular',
            'objetivo',
        ]
        labels = {
            'nome':'Nome completo',
            'nascimento':'Data de nascimento',
            'cep':'CEP',
            'endereco':'Endereço',
            'bairro':'Bairro',
            'cidade':'Cidade',
            'estado':'Estado',
            'sexo':'Sexo',
            'objetivo':'Objetivo',
            'celular':'Celular',
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),
            'endereco':forms.TextInput(attrs={'class':'form-control'}),
            'bairro':forms.TextInput(attrs={'class':'form-control'}),
            'cidade':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-select'}),
            'sexo':forms.Select(attrs={'class':'form-select'}),
            'objetivo':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'nascimento':forms.TextInput(attrs={'class':'form-control',
                                                'type':'date',}),
        }