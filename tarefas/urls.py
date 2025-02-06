from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('concluir/<int:tarefa_id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
