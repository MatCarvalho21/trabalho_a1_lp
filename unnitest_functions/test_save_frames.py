"""
Esse módulo tem como objetivo verificar o funcionamento da função 'save_frames', que pertence 
ao módulo 'matheus_vis.py'. Para resumir, a função recebe o objeto plot (visualização), o ano analizado, 
mes analizado e o caminho para a pasta onde a imagem deverá ser salva.
"""

import sys, os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "..", "functions")
sys.path.append(caminho_functions)

import matplotlib.pyplot as plt
import os
import unittest
import pandas as pd  
from utils import set_anabolizantes
from matheus_vis import save_frames, gerador_de_frames

######################################################################################################################

# dataframes para testes
df_01 = pd.read_csv("dados\Manipulados_2014_01.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_02 = pd.read_csv("dados\Manipulados_2014_02.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_03 = pd.read_csv("dados\Manipulados_2014_03.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
dataframe_geral = pd.concat((df_01, df_02, df_03))
dataframe_teste = set_anabolizantes(dataframe_geral)

dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Idade': [25, 30, 22, 35, 28],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}
dataframe_invalido = pd.DataFrame(dados)

figure_teste, valor = gerador_de_frames(dataframe_teste, "2014", "2")

######################################################################################################################

class TestSaveFrames(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_figure_esperada(self):
        """
        verifica o comportamento da função quando todos os parâmetros são passados de forma correta
        """
        self.assertEqual(save_frames(figure_teste, "2014", "2", "functions"), 'Deu tudo certo!')
        os.remove("functions\\frame_2014_2.png") #vai apagar o arquivo gerado durante o teste

    def test_figure_invalida(self):
        """
        verifica o comportamento da função caso não seja passado um objeto figure, no caso uma string
        """
        self.assertEqual(save_frames("Matheus", "2014", "2", "functions"), 'Não foi passado um objeto do tipo plt.figure. Verifique os parâmetros.')

    def test_datas_invalidas(self):
        """
        verifica o comportamento da função caso as datas sejam passadas em um formato inesperado
        """
        self.assertEqual(save_frames(figure_teste, "matheus", "2", "functions"), 'As datas fornecidas não estão no formato esperado. Verifique a documentação.')

    def test_pasta_inexistente(self):
        """
        verifica o comportamento da função 
        """
        self.assertEqual(save_frames(figure_teste, "2014", "2", "pasta inexistente genérica"), 'O path passado não corresponde à nenhuma pasta. Verifique os parâmetros.')

if __name__ == "__main__":
    unittest.main()