import sys
sys.path.append("C:\\Users\\mathe\\trabalho_a1_lp\\functions")

import unittest
import pandas as pd  
from gifs import seletor_de_frames

"""
Esse módulo tem como objetivo verificar o funcionamento da função 'seletor_de_frames', que pertence 
ao módulo 'gifs.py'. Para resumir, a função recebe um ano inicial, um ano final e um path para a pasta 
em questão. Essa pasta deve conter várias imagens, com nomes pré-definidos no seguinte formato: 
'frame_{ano}_{mês}.png'. Ele vai selecionar todos os frames nessa range de datas e retornar uma lista
com eles que será usada em outra função para montar um gif.
"""

class TestSeletorDeFrames(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_pasta_sem_frames(self):
        """
        verifica o comportamento da função quando uma pasta sem frames é fornecida
        """
        self.assertIsNone(seletor_de_frames("2014", "2015", "functions"))

    def test_pasta_inexistente(self):
        """
        verifica o comportameto da função quando é passado um path inválido (pasta inexistente)
        """
        self.assertIsNone(seletor_de_frames("2014", "2015", "pasta_inexistente_genérica"))

    def test_datas_invalidas(self):
        """
        verifica o comportamento da função quando são passadas as datas em um formato inválido,
        no caso foram testadas as datas por extenso, mas o mesmo valeria para qualquer formato
        """
        self.assertIsNone(seletor_de_frames("dois mil e quartoze", "dois mil e quinze", "functions\matheus_imagens"))

    def test_data_inicial_maior_que_data_final(self):
        """
        vai verificar como a função deve funcionar se um range inválido de datas for fornecido

        Obs.: acontece que o range é 'inválido', mas o código não quebra, é um range vazio
        isso significa que ele não itera sobre o range e não seleciona nenhum frame e 
        retorna uma lista vazia de frames
        """
        self.assertEqual(seletor_de_frames("2021", "1900", "functions\matheus_imagens"), [])

if __name__ == "__main__":
    unittest.main()