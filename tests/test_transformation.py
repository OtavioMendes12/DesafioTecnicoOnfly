import os
import sys

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analysis import calcular_medias_por_tipo

def test_calcular_medias_por_tipo():

    df_mock = pd.DataFrame([
        {"Tipos": ["Fogo"], "Ataque": 60, "Defesa": 50, "HP": 70},
        {"Tipos": ["Fogo"], "Ataque": 80, "Defesa": 60, "HP": 90},
        {"Tipos": ["Água"], "Ataque": 70, "Defesa": 55, "HP": 85},
    ])

    medias = calcular_medias_por_tipo(df_mock)


    fogo = medias[medias["Tipos"] == "Fogo"]
    agua = medias[medias["Tipos"] == "Água"]

    assert round(fogo["Ataque"].values[0], 2) == 70.0, "Média de ataque do tipo Fogo está incorreta"
    assert round(agua["Defesa"].values[0], 2) == 55.0, "Média de defesa do tipo Água está incorreta"