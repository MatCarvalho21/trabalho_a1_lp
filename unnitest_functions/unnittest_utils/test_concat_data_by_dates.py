"""
Esse módulo tem como objetivo verificar o funcionamento da função 'concat_data_by_dates', que pertence 
ao módulo 'utils.py'. A função recebe duas datas da forma "AAAAmm" com os 4 primeiros dígitos
sendo o ano e os últimos 2 o mês, e concatena da base de dados todos os dados entre estas duas datas,
sendo que é possível filtrar as colunas também.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from utils import concat_data_by_dates


class Test_Download_Csv_By_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_tipo_caso_basico(self):
        """
        verifica se a função retorna um DataFrame no caso báscio.
        """
        self.assertEqual(type(concat_data_by_dates("2014/01", "2014/01")), pd.DataFrame)

    def test_filtrar_colunas(self):
        """
        verifica se a função está filtrando as colunas corretamente.
        """
        self.assertEqual(concat_data_by_dates("2014/01", "2014/01", filtered_columns=["MES_VENDA"]).columns, ["MES_VENDA"])

    def test_data_invalida(self):
        """
        verifica se a função retorna uma lista vazia caso o tipo a data seja inválida,
        como ela possui a mesma validação da função validacao_datas,
        caso ela funcione corretamente, apenas um teste é necessário para validar.
        """
        self.assertIsNone(concat_data_by_dates("2013/01", "2014/01")) 

    def test_caminho_invalido(self):
        """
        verifica se o caminho digitado é válido ou não.
        """
        self.assertIsNone(concat_data_by_dates("2014/01", "2014/01", path="CAMINHO_INVÁLIDO"))

    def test_filtrar_colunas_invalidas(self):
        """
        verifica se caso a coluna de filtra seja inválida, continua retornando o dataframe.
        """
        self.assertEqual(type(concat_data_by_dates("2021/01", "2021/01", filtered_columns=3)), pd.DataFrame)


if __name__ == "__main__":
    unittest.main()