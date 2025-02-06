from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('ALTA', 'Alta'),
        ('MEDIA', 'Média'),
        ('BAIXA', 'Baixa'),
    ]

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDA', 'Concluída'),
    ]

    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição', blank=True, null=True)
    prioridade = models.CharField('Prioridade', max_length=10, choices=PRIORIDADE_CHOICES, default='BAIXA')
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    data_conclusao = models.DateTimeField('Data de Conclusão', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')

    class Meta:
        ordering = ['-prioridade', '-data_criacao']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"
