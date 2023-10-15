"""
Esse módulo tem como objetivo verificar o funcionamento da função 'get_dates_between_dates', que pertence 
ao módulo 'get_data.py'. A função recebe duas datas da forma "AAAAmm" com os 4 primeiros dígitos
sendo o ano e os últimos 2 o mês, e deve retornar uma lista com todas as datas
separadas por meses entre a primeira data e a segunda, no formato de
string "AAAAmm".
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from get_data import get_dates_between_dates


class Test_Get_Dates_Between_Dates(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_caso_base(self):
        """
        verifica se a função funciona no caso base, retornando a lista.
        """
        self.assertEqual(get_dates_between_dates("2014/01", "2014/01"), ['201401'])
        self.assertEqual(get_dates_between_dates("2021/08", "2021/11"), ['202108', '202109', '202110', '202111'])

    def test_tipo_data_invalido(self):
        """
        verifica se a função retorna uma lista vazia caso o tipo a data seja inválida,
        como ela possui a mesma validação da função validacao_datas,
        caso ela funcione corretamente, apenas um teste é necessário para validar.
        """
        self.assertEqual(get_dates_between_dates("2016/02", True), []) 


if __name__ == "__main__":
    unittest.main()