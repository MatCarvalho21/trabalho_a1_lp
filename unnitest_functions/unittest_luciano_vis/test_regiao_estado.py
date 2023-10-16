import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import pandas as pd  
from luciano_vis import regiao_estado

class TestSetAnabolizantes(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_resultados_esperados(self):
        self.assertEqual(regiao_estado("MG"), "Sudeste")
        self.assertEqual(regiao_estado("SC"), "Sul")
        self.assertEqual(regiao_estado("MT"), "Centro-Oeste")
        self.assertEqual(regiao_estado("TO"), "Norte")
        self.assertEqual(regiao_estado("BA"), "Nordeste")
        self.assertEqual(regiao_estado("Belo Horizonte"), None)

if __name__ == "__main__":
    unittest.main()