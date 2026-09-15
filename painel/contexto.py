from .models import ConfiguracaoEscola


def config_escola(request):
    """Disponibiliza a configuração da escola (sidebar/rodapé) em todos os templates."""
    try:
        return {'cfg_escola': ConfiguracaoEscola.atual()}
    except Exception:
        return {'cfg_escola': None}
