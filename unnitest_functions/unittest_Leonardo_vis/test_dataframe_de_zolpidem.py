"""
Módulo de testes unitários da função dataframe_de_zolpidem do módulo Leonardo_vis
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)
import unittest
import Leonardo_vis 
import utils
import pandas as pd


class TestDataFrameDeZolpidem(unittest.TestCase):
    def test_type_dataframe(self):
        self.assertIsInstance(Leonardo_vis.dataframe_de_zolpidem(dataframe_selecionado), pd.DataFrame)


if __name__ == '__main__':
    dataframe_selecionado = utils.concat_data_by_dates("2014/01", "2016/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"])

    unittest.main()