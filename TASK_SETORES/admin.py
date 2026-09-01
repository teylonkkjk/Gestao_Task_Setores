from django.contrib import admin
from .models import Setor, Membro, Task, Daily_Meeting, Daily_Note

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # list_display: Escolhe quais colunas vão aparecer na tabela principal
    list_display = ('usuario','setor','cargo')
    # list_filter: Cria um menu lateral para você filtrar os dados com 1 clique
    list_filter = ('cargo', 'setor')
    # search_fields: Cria uma barra de pesquisa no topo (busca pelo nome do usuário)
    search_fields = ('usuario__username',)
    
@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','data_criacao')

@admin.register(Daily_Note)
class DailyNoteAdmin(admin.ModelAdmin):
    list_display = ('autor', 'daily')
    # Como a daily é uma data/hora, podemos pesquisar pelas anotações do autor
    search_fields = ('autor__usuario__username',)
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # 1. Configurações Visuais
    list_display = ('titulo', 'status', 'prioridade', 'membro', 'setor')
    list_editable = ('status', 'prioridade')
    list_filter = ('status', 'prioridade', 'setor')
    search_fields = ('titulo', 'descricao')
    
    # 2. Regras de Segurança
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
            
        try:
            membro_logado = Membro.objects.get(usuario=request.user)
            if membro_logado.cargo in ['chefe', 'senior']:
                return True
        except Membro.DoesNotExist:
            pass
            
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
            
        try:
            membro_logado = Membro.objects.get(usuario=request.user)
            if membro_logado.cargo in ['chefe', 'senior']:
                return True
        except Membro.DoesNotExist:
            pass
            
        return False
       
@admin.register(Daily_Meeting)
class DailyMeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_agendada', 'setor') 
    #list_editable = ('membros')
    list_filter = ('setor', 'data_agendada')
    #list_filter = ('chefe','senior')
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        try:
            membro = Membro.objects.get(usuario=request.user)
            if membro.cargo in ['chefe', 'senior']:
                return True
        except Membro.DoesNotExist:
            pass
        return False
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
            
        try:
            membro = Membro.objects.get(usuario=request.user)
            if membro.cargo in ['chefe', 'senior']:
                return True
        except Membro.DoesNotExist:
            pass
            
        return False
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
            
        try:
            membro = Membro.objects.get(usuario=request.user)
            if membro.cargo in ['chefe', 'senior']:
                return True
        except Membro.DoesNotExist:
            pass
            
        return False