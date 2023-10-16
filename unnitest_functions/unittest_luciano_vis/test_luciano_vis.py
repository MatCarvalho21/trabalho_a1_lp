import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import pandas as pd  
from luciano_vis import luciano_vis

class TestLucianoVis(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_exceptions(self):
        self.assertRaises(ValueError, luciano_vis, "aa")
        self.assertRaises(ValueError, luciano_vis, "save", None)


if __name__ == "__main__":
    unittest.main()