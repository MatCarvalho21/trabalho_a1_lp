import unittest
import pandas as pd  
from utils import set_anabolizantes
from matheus_vis import gerador_de_frames

"""
Esse módulo tem como objetivo verificar o funcionamento da função 'gerador_de_frames', que pertence 
ao módulo 'matheus_vis.py'. Para resumir, a função recebe um dataframe tratado, e a data que será analisada, 
composta pelo ano e pelo mês. O objetivo da função é bem específico, ela não é feita para funcionar em vários
contextos. Ela vai salvar na pasta 'matheus_imagens' o frame gerado com o nome 'frame_{ano}_{mês}.png. Esse
frame contém um gráfico composto de três subgráficos que abordam a venda de esteroides e anabolizates na data fornecida.
"""

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

class TestGeradorDeFrames(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_dataframe_esperado(self):
        """
        verifica o comprotamento da função quando tudo, inclusive o dataframe passado, é válido
        """
        self.assertEqual(gerador_de_frames(dataframe_teste, 2014, 2), "Deu tudo certo!")

    def test_dataframe_vazio(self):
        """
        verifica o comportamento da função se um dataframe vazio for passado
        """
        self.assertEqual(gerador_de_frames(pd.DataFrame(), 2015, 5), "O dataframe está vazio.")

    def test_dataframe_invalido(self):
        """
        verifica o comportamento da função quando um dataframe diferente e não vazio é fornecido
        """
        self.assertEqual(gerador_de_frames(dataframe_invalido, 2015, 5), "O dataframe fornecido está em um formato inválido")

    def test_dataframe_inexistente(self):
        """
        verifica o comportamendo da função se algo diferente do dataframe esperado for passado 
        """
        self.assertEqual(gerador_de_frames("Matheus", 2015, 5), "Não foi fornecido um dataframe.")

    def test_ano_invalido(self):
        """
        verifica o comportamento da função quando um ano inválido é passado
        """
        self.assertEqual(gerador_de_frames(dataframe_teste, "Matheus", 5), "O ano fornecido deve ser um inteiro.")

    def test_mes_invalido(self):
        """
        verifica o comportamento da função quando um mês inválido é passado
        """
        self.assertEqual(gerador_de_frames(dataframe_teste, 2014, "Fillype"), "O mês fornecido deve ser um inteiro")

if __name__ == "__main__":
    unittest.main()