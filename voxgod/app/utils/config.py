# core/config.py

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

class Config:
    """
    Classe de configuração para armazenar variáveis globais.
    """
    APP_NAME = "ShadowData Voice System"
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    LANGUAGE = os.getenv("LANGUAGE", "pt-BR")
