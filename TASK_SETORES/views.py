from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Setor, Task, Membro, Daily_Meeting, Daily_Note
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def tela_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        usuario_banco = authenticate(request, username=usuario, password=senha)
        if usuario_banco is not None:
            login(request, usuario_banco)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Membro não encontrado ou senha incorreta')
            return redirect('login') 
    return render(request, 'login.html') 
        
@login_required(login_url='login')
def dashboard(request):
    meu_setor = request.user.setor
    tarefa_do_setor = Task.objects.filter(setor=meu_setor)
    hoje = timezone.now().date()
    proxima_daily = Daily_Meeting.objects.filter(
        setor=meu_setor,
        data_agendada__gte=hoje
    ).order_by('data_agendada', 'horario_da_daily').first()
    context = {
        'tarefas': tarefa_do_setor,
        'setor_atual': meu_setor,
        'proxima_daily': proxima_daily
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def cadastro_tarefas(request):
    if request.user.cargo not in ['senior', 'chefe']:
        messages.error(request, "Você não tem permissão para criar tarefas.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        data_entrega_digitada = request.POST.get('data_entrega') 
        id_do_membro = request.POST.get('membro_atribuido')
        membro_recebedor = Membro.objects.get(id=id_do_membro)
        
        Task.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            data_entrega=data_entrega_digitada, 
            setor=request.user.setor,
            responsavel=request.user,
            membro=membro_recebedor
        )
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('dashboard')
        
    equipe_do_setor = Membro.objects.filter(setor=request.user.setor)
    return render(request, 'cadastro_tarefa.html', {'equipe': equipe_do_setor})

@login_required(login_url='login')
def mudar_status_tarefa(request, task_id):
    tarefa = get_object_or_404(Task, id=task_id)
    
    if tarefa.setor != request.user.setor:
        messages.error(request, "Você não pode alterar tarefas de outro setor!")
        return redirect('dashboard')

    if request.method == 'POST':
        novo_status = request.POST.get('status')
        
        if request.user.cargo == 'estagiario' and novo_status == 'concluido':
            messages.error(request, "Estagiários não podem concluir tarefas sozinhos. Peça aprovação a um Sênior ou Chefe.")
            return redirect('dashboard')
            
        tarefa.status = novo_status
        tarefa.save()
        
        messages.success(request, "Status da tarefa atualizado!")
        return redirect('dashboard')