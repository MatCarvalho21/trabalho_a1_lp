"""
Esse módulo tem como objetivo verificar o funcionamento da função 'gera_visualizacao_cloroquina', que pertence 
ao módulo 'silla_vis.py'. A função recebe um dataframe, uma coluna com o que será contabilizado e uma coluna com 
estados, e então, retorna uma figura do matplotlib como mapa do Brasil sobre os estados como heatmap da quantidade
do que foi contabilizado.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
from sillas_vis import gera_visualizacao_cloroquina


class Test_Gera_Visualizacao_Cloroquina(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_data_frame_invalido(self):
        """
        verifica se a função não retorna nada caso o dataframe seja inválido.
        """

        self.assertIsNone(gera_visualizacao_cloroquina(66))
        self.assertIsNone(gera_visualizacao_cloroquina("Sphinx"))


    def test_colunas_invalidas(self):
        """
        verifica se a função não retorna nada caso a coluna seja inválida.
        """
        dados_teste = pd.DataFrame({'COLUNA_INVÁLIDA': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertIsNone(gera_visualizacao_cloroquina(dados_teste))


    def test_data_frame_vazio(self):
        """
        verifica se a função não retorna nada caso o dataframe esteja vazio.
        """
        self.assertIsNone(gera_visualizacao_cloroquina(pd.DataFrame()))


if __name__ == "__main__":
    unittest.main()