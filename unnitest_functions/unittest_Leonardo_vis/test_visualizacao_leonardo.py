"""
Módulo de testes unitários da função visualizacao_leonardo do módulo Leonardo_vis
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)
import unittest
import Leonardo_vis 
import utils
import pandas as pd


class TestVisualizacao(unittest.TestCase):
    
    def test_visualizacao_leonardo(self):
        self.assertEqual(Leonardo_vis.visualizacao_leonardo(dataframe_selecionado, esse_caminho), "Visualização finalizada!")


if __name__ == '__main__':
    dataframe_selecionado = utils.concat_data_by_dates("2014/01", "2016/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"])

    unittest.main()
