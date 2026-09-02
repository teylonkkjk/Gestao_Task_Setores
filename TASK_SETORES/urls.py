from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro-tarefa/', views.cadastro_tarefas, name='criar_tarefa'),
    path('mudar-status/<int:task_id>/', views.mudar_status_tarefa, name='mudar_status'),
]