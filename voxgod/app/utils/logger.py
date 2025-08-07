# core/logger.py

import logging

def get_logger(name: str):
    """
    Retorna um logger configurado com o nome do módulo.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add handler only once
    if not logger.handlers:
        logger.addHandler(ch)

    return logger
