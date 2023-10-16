"""
Esse módulo tem como objetivo verificar o funcionamento da função 'download_csv_by_dates', que pertence 
ao módulo 'get_data.py'. A função recebe duas datas da forma "AAAAmm" com os 4 primeiros dígitos
sendo o ano e os últimos 2 o mês, e baixa da base de dados um csv contendo todos os
dados entre a primeira e a segunda data, além de receber qual deve ser o arquivo de saída.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from get_data import download_csv_by_dates


class Test_Download_Csv_By_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_data_inválida(self):
        """
        verifica se a função retorna None caso o tipo a data seja inválida,
        como ela possui a mesma validação da função validacao_datas,
        caso ela funcione corretamente, apenas um teste é necessário para validar.
        """
        self.assertIsNone(download_csv_by_dates("2013/01", "2015/02"))

    def test_output_file_invalido(self):
        """
        verifica se a função retorna None caso o output_file seja inválido.
        """
        self.assertIsNone(download_csv_by_dates("2016/02", "2016/03", output_file=True)) 
        self.assertIsNone(download_csv_by_dates("2016/02", "2016/03", output_file="inválido.txt"))


if __name__ == "__main__":
    unittest.main()