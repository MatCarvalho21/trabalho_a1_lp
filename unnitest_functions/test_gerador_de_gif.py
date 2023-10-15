"""
Esse módulo tem como objetivo verificar o funcionamento da função 'gerador_de_gif', que pertence 
ao módulo 'gifs.py'. Para resumir, a função recebe uma lista de frames (imagens), uma pasta onde o gif 
deverá ser salvo, o nome do arquivo e o fps do gif. Caso tudo corra bem, a função vai salvar um gif
seguindo os parâmetros fornecidos.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "functions")
sys.path.append(caminho_functions)

import unittest
import os
import pandas as pd  
from gifs import seletor_de_frames, gerador_de_gif


# lista para testes
lista_de_frames = seletor_de_frames("2014", "2015", "functions\matheus_imagens")

class TestGeradorDeGif(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_lista_esperada(self):
        """
        verifica o comportamento da função quando fornecida uma lista válida com vários frames
        """
        self.assertEqual(gerador_de_gif(lista_de_frames, "functions", "meu_arquivo", 10), "Deu tudo certo!")
        os.remove("functions\meu_arquivo.gif") #vai apagar o arquivo gerado durante o teste

    def test_lista_vazia(self):
        """
        verifica o comportamento da função quando fornecida uma lista vazia, sem frames
        """
        self.assertIsNone(gerador_de_gif(list(), "functions", "meu_arquivo", 5))

    def test_lista_invalida(self):
        """
        verifica o comportamento da função quando fornecida uma lista inválida, com nomes por exemplo
        """
        self.assertIsNone(gerador_de_gif(["Matheus", "Sillas", "Luciano", "Leonardo"], "functions", "meu_arquivo", 5))


    def test_pasta_invalida(self):
        """
        verifica o comportamento da função quando fornecida uma pasta inexistente (inválida)
        """
        self.assertIsNone(gerador_de_gif(lista_de_frames, "pasta_inexistente", "meu_arquivo", 5))
        

    def test_fps_invalido(self):
        """
        verifica o comportamento da função quando fornecido um fps inválido, diferente de um inteiro
        """
        self.assertIsNone(gerador_de_gif(lista_de_frames, "functions", "meu_arquivo", "Nada"))

if __name__ == "__main__":
    unittest.main()