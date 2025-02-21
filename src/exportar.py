import os
import datetime
from src.logger import logger

def salvar_csv(df, nome_base):
    try:
        pasta_destino = "dados_exportados"

        os.makedirs(pasta_destino, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        nome_arquivo = os.path.join(pasta_destino, f"{nome_base}_{timestamp}.csv")

        df.to_csv(nome_arquivo, index=False)

        logger.info(f"Dados salvos com sucesso em {nome_arquivo}")
    except Exception as e:
        logger.error(f"Erro ao salvar CSV {nome_base}: {e}")