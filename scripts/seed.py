"""Popula o Organiza+ (dados de exemplo do original) e cria o usuário admin.
A senha gerada vai para /tmp/.organiza_pw (0600) para o script do Cofre registrar — nunca é impressa."""
import datetime
import os
import secrets
import sys

sys.path.insert(0, '/home/pi/python/organiza')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organiza_project.settings')
import django
django.setup()

from django.contrib.auth.models import User
from painel.models import Aula, ConfiguracaoEscola, EventoCalendario, Tarefa

cfg = ConfiguracaoEscola.atual()
cfg.escola, cfg.turma, cfg.periodo = 'E. E. Santa Olímpia', '3º ano B — Ensino Médio', 'Manhã · 07:00 às 12:20'
cfg.save()
print('config:', cfg.escola, '|', cfg.turma)

if Tarefa.objects.count() == 0:
    Tarefa.objects.create(titulo='Lista de exercícios — funções quadráticas', materia='Matemática',
                          entrega='2026-08-21', prioridade='alta')
    Tarefa.objects.create(titulo="Resenha do livro 'Vidas Secas'", materia='Literatura',
                          entrega='2026-08-25', prioridade='media')
    Tarefa.objects.create(titulo='Pesquisa sobre energias renováveis', materia='Geografia',
                          entrega='2026-09-02', prioridade='baixa', concluida=True)
    print('3 tarefas criadas')

if Aula.objects.count() == 0:
    grade = [('07:20', 'Matemática', 'Sala 12'), ('09:10', 'Biologia', 'Laboratório'),
             ('10:50', 'Educação Física', 'Quadra')]
    for dia in range(5):
        for ordem, (h, disc, local) in enumerate(grade):
            Aula.objects.create(dia_semana=dia, horario=h, disciplina=disc, local=local, ordem=ordem)
    print('cronograma criado (5 dias x 3 aulas)')

if EventoCalendario.objects.count() == 0:
    ano = datetime.date.today().year
    EventoCalendario.objects.create(data='%d-09-07' % ano, titulo='Feriado da Independência', letivo=False)
    EventoCalendario.objects.create(data='%d-10-15' % ano, titulo='Dia do Professor', letivo=False)
    EventoCalendario.objects.create(data='%d-11-20' % ano, titulo='Consciência Negra', letivo=False)
    print('eventos do calendario criados')

alfabeto = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
pw = ''.join(secrets.choice(alfabeto) for _ in range(14))
u, criado = User.objects.get_or_create(username='admin')
u.is_staff, u.is_superuser = True, True
u.set_password(pw)
u.save()
print('usuario admin:', 'criado' if criado else 'atualizado')

with open('/tmp/.organiza_pw', 'w') as f:
    f.write(pw)
os.chmod('/tmp/.organiza_pw', 0o600)
print('senha gravada em /tmp/.organiza_pw (0600) para o registro no Cofre')
