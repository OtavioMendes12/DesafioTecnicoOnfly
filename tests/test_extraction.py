import pytest
from src.extraction import extrair_dados


def test_extrair_dados():
    dados = extrair_dados()

    assert len(dados) == 100, "A extração deveria retornar 100 Pokémon"

    for pokemon in dados:
        assert "name" in pokemon, "Cada Pokémon deve ter um nome"
        assert "url" in pokemon, "Cada Pokémon deve ter uma URL"