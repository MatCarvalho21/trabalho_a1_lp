"""
Esse módulo tem como objetivo verificar o funcionamento da função 'mapeia_dados_estaduais', que pertence 
ao módulo 'silla_vis.py'. A função recebe um dataframe e uma coluna com estados, e então, retorna um dataframe
contendo a coluna deste atributo unidos aos dados do geobr, biblioteca usada para fazer
plotagens com o mapa brasileiro, no caso, dados estaduais.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd
import geopandas  
from sillas_vis import mapeia_dados_estaduais


class Test_Download_Csv_By_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_tipo_caso_basico(self):
        """
        verifica se a função retorna um DataFrame no caso básico.
        """
        dados_teste = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertEqual(type(mapeia_dados_estaduais(dados_teste, "UF")), geopandas.GeoDataFrame)


    def test_data_frame_invalido(self):
        """
        verifica se a função não retorna nada caso o dataframe seja inválido.
        """

        self.assertIsNone(mapeia_dados_estaduais(66, "UF"))


    def test_coluna_invalida(self):
        """
        verifica se a função não retorna nada caso a coluna seja inválida.
        """
        dados_teste = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertIsNone(mapeia_dados_estaduais(dados_teste, "COLUNA_INVÁLIDA"))


if __name__ == "__main__":
    unittest.main()