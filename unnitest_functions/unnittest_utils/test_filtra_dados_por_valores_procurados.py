"""
Esse módulo tem como objetivo verificar o funcionamento da função 'filtra_dados_por_valores_procurados', que pertence 
ao módulo 'utils.py'. A função recebe um dataframe, o nome de uma coluna e os valores procurados nela, e então, filtra
o dataframe para apenas as linhas com os valores procurados na coluna.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from utils import filtra_dados_por_valores_procurados


class Test_Download_Csv_By_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_tipo_caso_basico(self):
        """
        verifica se a função retorna um DataFrame no caso básico.
        """
        dados_teste = pd.DataFrame({"PINCIPIO_ATIVO": ["CLOROQUINA", "DIFOSFATO DE CLOROQUINA", "HIDROXICLOROQUINA", "IBUPROFENO"],
                                                "Qnt": [10, 5, 8, 15]})

        self.assertEqual(type(filtra_dados_por_valores_procurados(dados_teste, "PINCIPIO_ATIVO", "CLOROQUINA")), pd.DataFrame)
        self.assertEqual(type(filtra_dados_por_valores_procurados(dados_teste, "PINCIPIO_ATIVO", ["CLOROQUINA", "HIDROXICLOROQUINA"])["Qnt"]), pd.Series)
        

    def test_data_frame_invalido(self):
        """
        verifica se a função não retorna nada caso o dataframe seja inválido.
        """

        self.assertIsNone(filtra_dados_por_valores_procurados(66, "PINCIPIO_ATIVO", "CLOROQUINA"))

    def test_coluna_invalida(self):
        """
        verifica se a função não retorna nada caso a coluna seja inválida.
        """
        dados_teste = pd.DataFrame({"PINCIPIO_ATIVO": ["CLOROQUINA", "DIFOSFATO DE CLOROQUINA", "HIDROXICLOROQUINA", "IBUPROFENO"],
                                                "Qnt": [10, 5, 8, 15]})

        self.assertIsNone(filtra_dados_por_valores_procurados(dados_teste, 13, "CLOROQUINA"))
    
        self.assertIsNone(filtra_dados_por_valores_procurados(dados_teste, "COLUNA_INVÁLIDA", "CLOROQUINA"))


if __name__ == "__main__":
    unittest.main()