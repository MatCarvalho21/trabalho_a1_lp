"""
Esse módulo tem como objetivo verificar o funcionamento da função 'soma_vendas_por_atributo', que pertence 
ao módulo 'silla_vis.py'. A função recebe um dataframe e um atributo, e então, retorna um dataframe
contendo a coluna deste atributo como valores únicos e a sua respectiva quantidade de observações
na coluna "vendas".
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from sillas_vis import soma_vendas_por_atributo


class Test_Download_Csv_By_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_tipo_caso_basico(self):
        """
        verifica se a função retorna um DataFrame no caso básico.
        """
        dados_teste = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertEqual(type(soma_vendas_por_atributo(dados_teste, "UF")), pd.DataFrame)


    def test_data_frame_invalido(self):
        """
        verifica se a função não retorna nada caso o dataframe seja inválido.
        """

        self.assertIsNone(soma_vendas_por_atributo(66, "UF"))


    def test_coluna_invalida(self):
        """
        verifica se a função não retorna nada caso a coluna seja inválida.
        """
        dados_teste = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertIsNone(soma_vendas_por_atributo(dados_teste, "COLUNA_INVÁLIDA"))


    def test_soma_correta(self):
        """
        verifica se a realiza retorna como valor mais frequência o estado correto (RJ).
        """
        dados_teste = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})

        self.assertEqual(soma_vendas_por_atributo(dados_teste, "UF")["UF"][0], "RJ")


if __name__ == "__main__":
    unittest.main()