from django.db import models


class ConfiguracaoEscola(models.Model):
    """Informações escolares mostradas no rodapé do painel e na sidebar."""
    escola = models.CharField('Escola', max_length=120, default='E. E. Santa Olímpia')
    turma = models.CharField('Turma', max_length=80, default='3º ano B — Ensino Médio')
    periodo = models.CharField('Período', max_length=80, default='Manhã · 07:00 às 12:20')
    tema_claro = models.BooleanField('Tema claro', default=False)

    class Meta:
        verbose_name = 'Configuração da escola'
        verbose_name_plural = 'Configuração da escola'

    def __str__(self):
        return self.escola

    @classmethod
    def atual(cls):
        obj = cls.objects.first()
        if obj is None:
            obj = cls.objects.create()
        return obj


class Tarefa(models.Model):
    PRIORIDADES = [('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')]

    titulo = models.CharField('Título', max_length=160)
    materia = models.CharField('Matéria', max_length=80)
    entrega = models.DateField('Entrega')
    prioridade = models.CharField('Prioridade', max_length=10, choices=PRIORIDADES, default='media')
    concluida = models.BooleanField('Concluída', default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['concluida', 'entrega', '-id']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.titulo


class Aula(models.Model):
    DIAS = [(0, 'Segunda'), (1, 'Terça'), (2, 'Quarta'), (3, 'Quinta'),
            (4, 'Sexta'), (5, 'Sábado'), (6, 'Domingo')]

    dia_semana = models.IntegerField('Dia da semana', choices=DIAS, default=0)
    horario = models.TimeField('Horário')
    disciplina = models.CharField('Disciplina', max_length=80)
    local = models.CharField('Local', max_length=80, blank=True)
    ordem = models.IntegerField('Ordem', default=0)

    class Meta:
        ordering = ['horario', 'ordem']
        verbose_name = 'Aula'
        verbose_name_plural = 'Cronograma'

    def __str__(self):
        return '%s %s — %s' % (self.get_dia_semana_display(), self.horario.strftime('%H:%M'), self.disciplina)


class EventoCalendario(models.Model):
    data = models.DateField('Data', unique=True)
    titulo = models.CharField('Título', max_length=120, blank=True)
    descricao = models.TextField('Descrição', blank=True)
    letivo = models.BooleanField('Dia letivo', default=True)

    class Meta:
        ordering = ['data']
        verbose_name = 'Evento do calendário'
        verbose_name_plural = 'Calendário'

    def __str__(self):
        return '%s — %s' % (self.data, self.titulo or 'evento')
