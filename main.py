from extraction import extrair_dados, processar_pokemon
from transformation import transformar_dados
from analysis import contar_tipos, calcular_medias_por_tipo, encontrar_top_5_experiencia, gerar_grafico
from exportar import salvar_csv
from logger import logger

def executar_pipeline():
    logger.info("Iniciando pipeline de dados dos Pokémon")

    try:
        urls = extrair_dados()
        if not urls:
            raise Exception("Falha na extração de URLs dos Pokémon")

        dados_brutos = processar_pokemon(urls)
        if not dados_brutos:
            raise Exception("Nenhum dado foi coletado dos Pokémon")

        df = transformar_dados(dados_brutos)
        if df.empty:
            raise Exception("Transformação falhou! DataFrame está vazio")

        df_tipos = contar_tipos(df)
        df_medias_tipos = calcular_medias_por_tipo(df)
        df_top_5_exp = encontrar_top_5_experiencia(df)

        gerar_grafico(df_tipos)
        salvar_csv(df, "pokemon_dados")
        salvar_csv(df_tipos, "pokemon_tipos")
        salvar_csv(df_medias_tipos, "medias_por_tipo")
        salvar_csv(df_top_5_exp, "top_5_experiencia")

        logger.info("Pipeline concluído com sucesso!")

    except Exception as e:
        logger.critical(f"ERRO CRÍTICO: {e}")
        logger.info("Encerrando o pipeline devido a erro crítico.")

if __name__ == "__main__":
    executar_pipeline()