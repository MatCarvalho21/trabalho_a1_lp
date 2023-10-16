import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import pandas as pd  
import pandas.testing as pd_testing
from luciano_vis import cria_datetime
import numpy as np

class TestCriaDatetime(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    
    def test_exceptions(self):
        dataframe_1 = pd.DataFrame({"ano": [2020, 2021, 2022], "mes": [1,2,3]})
        self.assertRaises(KeyError, cria_datetime, dataframe_1)

    def test_resultados_esperados(self):
        dataframe = pd.DataFrame({"ANO_VENDA": [2020, 2021, 2022], "MES_VENDA": [1,2,3]})
        self.assertIsInstance(cria_datetime(dataframe), pd.Series)


if __name__ == "__main__":
    unittest.main()