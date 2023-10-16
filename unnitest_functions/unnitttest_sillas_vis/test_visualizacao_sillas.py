"""
Esse módulo tem como objetivo verificar o funcionamento da função 'visualizacao_sillas', que pertence 
ao módulo 'silla_vis.py'. A função recebe duas datas e a pasta onde deverão ser salvas as visualizações
e gera diversas visualizações seguindo a função gera visualizações cloroquina, para cada data entre a data
inicial e a data final, as salvando na pasta destinada.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
from sillas_vis import visualizacao_sillas


class Test_Visualizacao_Sillas(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_data_invalida(self):
        """
        verifica se a função não retorna nada caso o dataframe seja inválido.
        """

        self.assertIsNone(visualizacao_sillas("2015/01", 42, "pasta_genérica"))
        self.assertIsNone(visualizacao_sillas("Sphinx", "2019/05", "pasta_genérica"))
        self.assertIsNone(visualizacao_sillas("2015/01", "2030/02", "pasta_genérica"))
        self.assertIsNone(visualizacao_sillas("2015/01", "2014/02", "pasta_genérica"))


    def test_diretório_inválido(self):
        """
        verifica se a função não retorna nada caso o diretório de saída seja inválido.
        """
    
        self.assertIsNone(visualizacao_sillas("2015/01", "2015/01", "DIRETÓRIO_INVÁLIDO"))


if __name__ == "__main__":
    unittest.main()