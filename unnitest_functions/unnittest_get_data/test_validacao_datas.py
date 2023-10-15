"""
Esse módulo tem como objetivo verificar o funcionamento da função 'gerador_de_gif', que pertence 
ao módulo 'gifs.py'. Para resumir, a função recebe uma lista de frames (imagens), uma pasta onde o gif 
deverá ser salvo, o nome do arquivo e o fps do gif. Caso tudo corra bem, a função vai salvar um gif
seguindo os parâmetros fornecidos.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from get_data import validacao_datas


class Test_Validacao_Datas(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """
    def test_caso_base(self):
        """
        verifica se a função funciona no caso base, retornando True para caso sim.
        """
        self.assertEqual(validacao_datas("2014/01", "2014/01"), True)
        self.assertEqual(validacao_datas("2015-02", "202111"), True)

    def test_tipo_data_invalido(self):
        """
        verifica se a função não retorna nada caso o tipo seja incorreto.
        """
        self.assertIsNone(validacao_datas("2016/02", True))
        self.assertIsNone(validacao_datas(2015, "2016/02"))
        self.assertIsNone(validacao_datas("2015", "20162"))  
        self.assertIsNone(validacao_datas("inválido", "2016/02"))

    def test_data_final_maior_que_incial(self):
        """
        verifica se a função não retorna nada caso a data final seja maior
        que a inicial.
        """
        self.assertIsNone(validacao_datas("2017/01", "2014/05"))
           

    def test_data_fora_do_intervalo(self):
        """
        verifica se a função não valida uma data fora do intervalo.
        """
        self.assertIsNone(validacao_datas("2014/01", "2022/01"))


if __name__ == "__main__":
    unittest.main()