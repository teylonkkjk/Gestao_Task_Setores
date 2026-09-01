from django.contrib import messages
from django.shortcuts import render
from .models import Setor, Task, Membro,Daily_Meeting,Daily_Note
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def tela_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        usuario_banco = authenticate(request, username = usuario, password = senha)
        if usuario_banco is not None:
            login (request, usuario_banco)
            return redirect ('')
        else:
            messages.error(request,'Membro não encontrado ou senha incorreta')
            return redirect('')
    return render(request, '')
        
@login_required(login_url='login')
def dashboard(request):
    meu_setor = request.user.setor
    tarefa_do_setor = Task.objects.filter(setor = meu_setor)
    context = {
        'tarefas': tarefa_do_setor,
        'setor_atual': meu_setor
    }
    return render(request, '', context)

@login_required(login_url='login')
def cadastro_tarefas(request):
    if request.user.cargo not in ['senior', 'chefe']:
        messages.error(request, "Você não tem permissão para criar tarefas.")
        return redirect('dashboard')
    if request.method == 'POST':
        titulo = request.POST.get('Titulo')
        descricao = request.POST.get('Descrição')
        prioridade = request.POST.get('prioridade')
        id_do_membro = request.POST.get('membro_atribuido')
        membro_recebedor = Membro.objects.get(id=id_do_membro)
        data_entrega_digitada = request.POST.get('data_entrega') 
        Task.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            data_entrega=data_entrega_digitada, 
        )
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('dashboard')
    
