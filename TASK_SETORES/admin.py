from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Setor, Membro, Task, Daily_Meeting, Daily_Note
admin.site.register(Setor)

# 1. Registrando o Membro com UserAdmin
@admin.register(Membro)
class MembroAdmin(UserAdmin):
    list_display = ('username', 'setor', 'cargo', 'is_staff')
    list_filter = ('cargo', 'setor')
    
    # Isso faz os campos "cargo" e "setor" aparecerem na tela de edição lá no painel!
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do Setor', {'fields': ('cargo', 'setor')}),
    )

@admin.register(Daily_Note)
class DailyNoteAdmin(admin.ModelAdmin):
    list_display = ('autor', 'daily')
    search_fields = ('autor__username',) # Atualizado de autor__usuario__username

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'membro', 'setor')
    list_editable = ('status', 'prioridade')
    list_filter = ('status', 'prioridade', 'setor')
    search_fields = ('titulo', 'descricao')
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        # Como o request.user é o Membro, basta ler o cargo direto!
        if request.user.cargo in ['chefe', 'senior']:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        if request.user.cargo in ['chefe', 'senior']:
            return True
        return False

@admin.register(Daily_Meeting)
class DailyMeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_agendada', 'setor') 
    list_filter = ('setor', 'data_agendada')
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.cargo in ['chefe', 'senior']:
            return True
        return False
        
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        if request.user.cargo in ['chefe', 'senior']:
            return True
        return False
        
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.cargo in ['chefe', 'senior']:
            return True
        return False