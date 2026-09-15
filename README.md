# 🗂️ Organiza+ — planner escolar (clone)

Clone funcional do app **Organiza+** (planejador do estudante), feito em **Django 4.2 + MySQL/MariaDB + Bootstrap 5**, rodando no pip5 na porta **8022**.

> Interface reproduzida a partir do app original (mesmas telas: **Painel**, **Calendário Anual** e **Configurações**), com as mesmas fontes (**Sora** + **Manrope**) e a paleta teal.

## Telas

| Tela | O que tem |
|---|---|
| **Painel** | **Tarefas** (título, matéria, entrega, prioridade alta/média/baixa — criar/editar/concluir/excluir), **Cronograma Hoje** (aulas do dia da semana) e **Informações escolares** (escola, turma, período) |
| **Calendário Anual** | 12 meses do ano, navegação de ano e edição por dia (título, descrição, dia letivo) |
| **Configurações** | Dados da escola/turma/período, tema claro e conta (sair) |

## Stack

- **Django 4.2** (LTS) + **MySQL/MariaDB** (`organiza` DB)
- **Bootstrap 5** + CSS próprio (`static/painel/organiza.css`) com a paleta do original
- Fontes Google: **Sora** (títulos) e **Manrope** (texto)
- Login com `django.contrib.auth` (usuário `admin`)

## Rodando

```bash
cd /home/pi/python/organiza
./venv/bin/python manage.py migrate
./venv/bin/python scripts/seed.py        # dados de exemplo + usuário admin (senha -> Cofre)
./venv/bin/python manage.py runserver 0.0.0.0:8022 --noreload
```

Em produção roda como **serviço systemd**: `organiza.service` (porta 8022), com o `.env` carregado por `EnvironmentFile`.

## Configuração (`.env`, não versionado)

```
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=0
DB_NAME=organiza
DB_USER=organiza
DB_PASSWORD=...      # no Cofre (entrada "organiza mysql")
DB_HOST=127.0.0.1
DB_PORT=3306
```

A senha do usuário web (`admin`) fica no **Cofre** (entrada `organiza web`).

## Estrutura

```
organiza/
├── organiza_project/     # settings/urls do projeto Django
├── painel/               # app: models, views, urls, contexto
├── templates/painel/     # base, painel, calendario, configuracoes, login
├── static/painel/        # organiza.css (paleta/fontes do original)
└── scripts/seed.py       # dados de exemplo + usuário admin
```

## Pendências / próximos passos

- [ ] Revisar fidelidade visual lado a lado com o original
- [ ] Autenticação multiusuário (hoje: um usuário `admin`)
- [ ] Aulas por dia da semana editáveis pela interface (hoje a grade é semeada por `seed.py`)
- [ ] Exportar/importar dados (JSON/CSV)
