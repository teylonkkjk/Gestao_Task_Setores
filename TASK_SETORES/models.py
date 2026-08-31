from django.db import models
from django.contrib.auth.models import User

class Setor(models.Model):
    nome = models.CharField('Nome',max_length=255, blank=False)
    descricao = models.CharField('Descrição', max_length=255, blank=False)
    data_criacao = models.DateTimeField('Data Criação', auto_now=True)
    membros = models.ManyToManyField(User,through='Membro', related_name='Setores')
    def __str__(self):
     return self.nome
    
class Membro(models.Model):
   CARGOS = (
        ('estagiario', 'Estagiário'),
        ('junior', 'Júnior'),
        ('senior', 'Sênior'),
        ('chefe', 'Chefe de Setor'),
    )
   usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
   cargo = models.CharField(max_length=20, choices=CARGOS, default='junior')
   class Meta:
       unique_together = ('usuario','setor')
   def __str__(self):
     return f'{self.usuario.username} - {self.cargo}'

class Task(models.Model):
    STATUS =(
        ('a fazer','A Fazer'),
        ('em processo','Em Processo'),
        ('concluido','Concluido')
        
    )
    PRIORIDADE =(
        ('relevante','Relevante'),
        ('mediana','Mediana'),
        ('extrema','Extrema')
        
    )
    titulo = models.CharField('Titulo',max_length=255, blank=False)
    descricao = models.TextField('Descrição', blank=False)
    status = models.CharField(max_length=20, choices=STATUS, default='a fazer')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE, default='relevante')
    data_entrega = models.DateField('Data de Entrega', null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, related_name='tasks')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_criadas')
    membro = models.ForeignKey(Membro,on_delete=models.CASCADE, related_name='tasks_atribuidas')
    def __str__(self):
        return f'{self.titulo} - {self.descricao} - {self.membro.usuario.username}'
    
class Daily_Meeting(models.Model):
    data_agendada = models.DateField('Data Agendada', blank=False, null=False)
    horario_da_daily = models.TimeField('Horário da Daily', null=True,blank=True)
    link_reuniao = models.URLField('Link da Chamada', max_length=1000, blank=False, null=False)
    resumo_pauta = models.TextField('Pauta / Resumo', blank=True, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE,related_name='dailies')
    organizador_da_daily = models.ForeignKey(User,on_delete=models.CASCADE, related_name='dailies_agendadas')
    class Meta:
        ordering = ['-horario_da_daily']
    def __str__(self):
        return f"Daily {self.setor.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
    
class Daily_Note(models.Model):
    feito_ontem = models.TextField('Feito Ontem', blank=True, null=True )
    planejamento_hoje = models.TextField('Planejamento de Hoje', blank=True, null=True)
    impedimentos = models.TextField('Impedimentos', null=True, blank=True)
    daily = models.ForeignKey(Daily_Meeting, on_delete=models.CASCADE, related_name='notas')
    autor = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='minhas_notas')
    def __str__(self):
        return f"Nota de {self.autor.user.username} na Daily {self.daily.id}"
    
    
    
   

   
    
    


