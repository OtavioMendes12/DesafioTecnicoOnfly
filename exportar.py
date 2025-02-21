import os
import datetime
from logger import logger

def salvar_csv(df, nome_base):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"{nome_base}_{timestamp}.csv"
        df.to_csv(nome_arquivo, index=False)
        logger.info(f"Dados salvos com sucesso em {nome_arquivo}")
    except Exception as e:
        logger.error(f"Erro ao salvar CSV {nome_base}: {e}")