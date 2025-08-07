# utils/helpers.py

def format_text(text: str) -> str:
    """
    Formata o texto para remover espaços extras e corrigir capitalização.
    """
    return text.strip().capitalize()

def is_exit_command(text: str) -> bool:
    """
    Verifica se o comando de voz é para encerrar.
    """
    return text.lower() in ["sair", "encerrar", "fechar", "parar"]
