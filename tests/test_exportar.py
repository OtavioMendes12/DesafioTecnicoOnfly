import os
import sys

import pandas as pd

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.exportar import salvar_csv

def test_salvar_csv():
    df_mock = pd.DataFrame({"Nome": ["Pikachu", "Charizard"], "Ataque": [55, 84]})
    salvar_csv(df_mock, "teste_pokemon")


    arquivos = os.listdir("dados_exportados")
    encontrou = any("teste_pokemon" in nome for nome in arquivos)

    assert encontrou, "O arquivo CSV não foi criado corretamente"