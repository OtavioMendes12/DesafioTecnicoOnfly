import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from logger import logger


def contar_tipos(df):

    try:
        tipos_contagem = Counter([tipo for tipos in df["Tipos"] for tipo in tipos])
        return pd.DataFrame(tipos_contagem.items(), columns=["Tipo", "Quantidade"])

    except Exception as e:
        logger.error(f"Erro ao contar tipos de Pokemon: {e}")
        return pd.DataFrame()


def calcular_medias_por_tipo(df):

    try:
        logger.info("Calculando medias por tipo de Pokémon")


        df_exploded = df.explode("Tipos")


        medias_df = df_exploded.groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().round(2).reset_index()

        logger.info("Medias calculadas com sucesso")
        return medias_df

    except Exception as e:
        logger.error(f"Erro ao calcular medias por tipo: {e}")
        return pd.DataFrame()


def encontrar_top_5_experiencia(df):
    try:
        logger.info("Encontrando os 5 Pokemon com maior experiencia base")
        top_5 = df.nlargest(5, "Experiencia Base")

        logger.info(f"Top 5 Pokemon com maior experiencia base encontrados")
        return top_5

    except Exception as e:
        logger.error(f"Erro ao encontrar os Pokemon com maior experiencia: {e}")
        return pd.DataFrame()


def gerar_grafico(df_tipos):

    try:
        logger.info("Gerando gráfico de distribuição de Pokémon por tipo")

        plt.figure(figsize=(12, 6))
        ax = sns.barplot(data=df_tipos, x="Tipo", y="Quantidade", palette="viridis")


        for p in ax.patches:
            ax.annotate(
                f"{int(p.get_height())}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10, color='black', fontweight='bold'
            )

        plt.xticks(rotation=45)
        plt.xlabel("Tipo de Pokémon")
        plt.ylabel("Quantidade")
        plt.title("Distribuição de Pokémon por Tipo")

        plt.savefig("pokemon_por_tipo_grafico.png")
        logger.info("Gráfico salvo como 'pokemon_por_tipo_grafico.png'")
        plt.show()

    except Exception as e:
        logger.error(f"Erro ao gerar gráfico: {e}")