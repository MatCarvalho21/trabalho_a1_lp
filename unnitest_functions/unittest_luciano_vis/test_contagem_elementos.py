import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import pandas as pd  
from luciano_vis import contagem_elementos
import numpy as np

class TestContagemElementos(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_tipos(self):
        dataframe = pd.DataFrame({"ANO_VENDA": [2020, 2021, 2022], "MES_VENDA": [1,2,3]})
        self.assertIsInstance(contagem_elementos(dataframe, "ANO_VENDA", "anos"), pd.Series)

    def test_atributos(self):
        dataframe = pd.DataFrame({"ANO_VENDA": [2020, 2021, 2022], "MES_VENDA": [1,2,3]})
        resultado = contagem_elementos(dataframe, "ANO_VENDA", "anos")

        self.assertEqual(resultado.name, "anos")
        self.assertEqual(resultado.size, 3)


if __name__ == "__main__":
    unittest.main()