from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarefa
from datetime import datetime

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        
        tarefa = Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            usuario=request.user
        )
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('tarefas:lista_tarefas')
    
    return render(request, 'tarefas/criar_tarefa.html')

@login_required
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    tarefa.status = 'CONCLUIDA'
    tarefa.data_conclusao = datetime.now()
    tarefa.save()
    messages.success(request, 'Tarefa concluída com sucesso!')
    return redirect('tarefas:lista_tarefas')

@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('tarefas:lista_tarefas')
