from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entrada do Diário'
        verbose_name_plural = 'Entradas do Diário'

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"

class PasswordStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Senha'
        verbose_name_plural = 'Senhas'

    def __str__(self):
        return f"{self.service_name} - {self.user.username}"

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Disciplina', max_length=100)
    value = models.DecimalField('Nota', max_digits=4, decimal_places=2)
    date = models.DateField('Data')
    notes = models.TextField('Observações', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return f"{self.subject} - {self.value}"

class TierList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tier List'
        verbose_name_plural = 'Tier Lists'

    def __str__(self):
        return self.name

class TierItem(models.Model):
    TIER_CHOICES = [
        ('S', 'S - Excepcional'),
        ('A', 'A - Ótimo'),
        ('B', 'B - Bom'),
        ('C', 'C - Médio'),
        ('D', 'D - Ruim'),
        ('F', 'F - Péssimo'),
    ]

    tierlist = models.ForeignKey(TierList, on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Nome', max_length=100)
    tier = models.CharField('Tier', max_length=1, choices=TIER_CHOICES)
    description = models.TextField('Descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['tier', 'created_at']
        verbose_name = 'Item da Tier List'
        verbose_name_plural = 'Itens da Tier List'

    def __str__(self):
        return f"{self.name} - {self.get_tier_display()}"

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField('Endereço IP')
    last_activity = models.DateTimeField('Última Atividade', auto_now=True)
    user_agent = models.TextField('User Agent')
    path = models.CharField('Caminho', max_length=255)
    
    class Meta:
        verbose_name = 'Atividade do Usuário'
        verbose_name_plural = 'Atividades dos Usuários'
        ordering = ['-last_activity']

    def __str__(self):
        return f"{self.user.username} - {self.ip_address} - {self.last_activity}"
