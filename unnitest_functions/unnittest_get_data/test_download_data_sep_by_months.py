"""
Esse módulo tem como objetivo verificar o funcionamento da função 'download_data_sep_by_months', que pertence 
ao módulo 'get_data.py'. A função recebe duas datas da forma "AAAAmm" com os 4 primeiros dígitos
sendo o ano e os últimos 2 o mês, um caminho, e baixa da base de dados e baixa da base de dados
todos os registros entre a primeira e a última data no cmainho definido.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from get_data import download_data_sep_by_months


class Test_Download_Data_Sep_By_Months(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_data_inválida(self):
        """
        verifica se a função retorna None caso o tipo a data seja inválida,
        como ela possui a mesma validação da função validacao_datas,
        caso ela funcione corretamente, apenas um teste é necessário para validar.
        """
        self.assertIsNone(download_data_sep_by_months("2013/01", "2015/02", "./test.csv"))

    def test_output_file_invalido(self):
        """
        verifica se a função retorna None caso o caminho seja inválido.
        """
        self.assertIsNone(download_data_sep_by_months("2016/02", "2016/04", True)) 
        self.assertIsNone(download_data_sep_by_months("2016/02", "2016/04", 3))


if __name__ == "__main__":
    unittest.main()