import pandas as pd
from logger import logger


def categorizar_experiencia(exp):
    try:
        if exp < 50:
            return "Fraco"
        elif exp <= 100:
            return "Médio"
        else:
            return "Forte"
    except Exception as e:
        logger.error(f"Erro ao categorizar experiência: {e}")
        return "Desconhecido"


def transformar_dados(pokemon_data):
    try:
        logger.info("Transformando os dados")
        df = pd.DataFrame(pokemon_data)
        df["Categoria"] = df["Experiencia Base"].apply(categorizar_experiencia)
        return df
    except Exception as e:
        logger.error(f"Erro na transformação de dados: {e}")
        return pd.DataFrame()