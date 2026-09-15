from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from .models import Aluno
from .forms import UserForm, AlunoForm


# Create your views here.

# def lista_aluno(request):
#     alunos = Aluno.objects.all()
#     return  render(request,
#                    'usuarios/aluno/lista.html',
#                    {'alunos' : alunos})

def dashboard_aluno(request):
    return render(request, 'usuarios/aluno/dashboard.html')

class AlunoListView(ListView):
    model = Aluno
    template_name = 'usuarios/aluno/lista.html'
    context_object_name = 'alunos'


#usuários/views
def criar_aluno(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        aluno_form = AlunoForm(request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save()
                    aluno = aluno_form.save(commit=False)
                    aluno.user = user
                    aluno.save()
                messages.success(request,
                                 'Aluno cadastrado com sucesso!')
                return redirect('usuarios:aluno_lista')
            except Exception:
                messages.error(request,
                               'Não foi possível cadastrar o Aluno!')
    else:
        user_form = UserForm()
        aluno_form = AlunoForm()
    return render(request, 'usuarios/aluno/form.html',{
        'user_form':user_form,
        'aluno_form':aluno_form,
    })

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST, instance=aluno)
        if aluno_form.is_valid():
            aluno_form.save()
            return redirect('usuarios:aluno_lista')
    else:
        aluno_form = AlunoForm(instance=aluno)
    return render(request, 'usuarios/aluno/form.html',
                  {'aluno_form':aluno_form}
                  )
class AlunoDetalhes(DetailView):
    model = Aluno
    template_name = 'usuarios/aluno/detalhe.html'
    context_object_name = 'aluno'


@require_POST
def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    user = aluno.user
    try:
        user.delete()
        messages.success(request,'Aluno excluido com sucesso!')
    except Exception:
        messages.error(request, 'não foi possível excuir o Aluno!')
    return redirect('usuarios:aluno_lista')