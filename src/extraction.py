
import requests
from src.logger import logger


def extrair_dados():
    try:
        logger.info("Iniciando extração de dados da PokeAPI")

        url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Erro ao acessar a API. Código HTTP: {response.status_code}")

        data = response.json()

        pokemon_dados = [{"name": pokemon["name"], "url": pokemon["url"]} for pokemon in data["results"]]

        logger.info(f"Extração concluída! {len(pokemon_dados)} Pokémon coletados")
        return pokemon_dados

    except Exception as e:
        logger.error(f"Falha na extração de dados: {e}")
        return []


def processar_pokemon(pokemon_urls):

    try:
        logger.info("Coletando detalhes dos Pokémon")
        pokemon_data = []
        for url in pokemon_urls:
            response = requests.get(url["url"])
            if response.status_code != 200:
                logger.warning(f"Erro ao buscar detalhes do Pokémon: {url}")
                continue
            details = response.json()

            pokemon_data.append({
                "ID": details["id"],
                "Nome": details["name"].capitalize(),
                "Experiencia Base": details.get("base_experience", 0),
                "Tipos": [t["type"]["name"].capitalize() for t in details["types"]],
                "HP": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "hp"), 0),
                "Ataque": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "attack"), 0),
                "Defesa": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "defense"), 0)
            })

        logger.info(f"{len(pokemon_data)} Pokémon processados com sucesso.")
        return pokemon_data

    except Exception as e:
        logger.error(f"Erro ao processar detalhes dos Pokémon: {e}")
        return []