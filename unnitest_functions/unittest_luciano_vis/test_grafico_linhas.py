import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import pandas as pd  
from luciano_vis import grafico_linhas
import numpy as np

class TestGraficoLinhas(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_exceptions(self):
        datas = [np.datetime64("2005-02-01"), np.datetime64("2005-05-01"), np.datetime64("2002-02-01"), np.datetime64("2003-02-01")]
        valores_1 = [2, 3, 1, 4]
        labels_1 = "label"
        alpha_1 = "1"
        self.assertRaises(TypeError, grafico_linhas, datas, valores_1, labels_1, None, alpha_1)

        valores_2 = ([2, 3, 1, 4], [2, 3, 2, 1])
        labels_2 = "label"
        self.assertRaises(ValueError, grafico_linhas, datas, valores_2, labels_2, None, 0.5)

        valores_3 = ([2, 3, 1, 4], [2, 3, 2])
        labels_3 = ("label", "label")
        self.assertRaises(ValueError, grafico_linhas, datas, valores_3, labels_3, None, 1)



if __name__ == "__main__":
    unittest.main()