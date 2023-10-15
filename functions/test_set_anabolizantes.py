import unittest
import pandas as pd  
from utils import set_anabolizantes

"""
Esse módulo tem como objetivo verificar o funcionamento da função 'set_anabolizantes', que pertence 
ao módulo 'utils.py'. Para resumir, a função em questão recebe um dataframe bruto, concatenado 
ou não, desde que seja um dataframe da base de dados dos medicamentos manipulados que foi analizada ao 
longo do trabalho. Ela vai retornar um dataframe filtrado com apenas os dados referentes aos hormônios 
esteroides e anabolizantes.
"""

#dataframes para testes
df_01 = pd.read_csv("dados\Manipulados_2014_01.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_02 = pd.read_csv("dados\Manipulados_2014_02.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_03 = pd.read_csv("dados\Manipulados_2014_03.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
dataframe_geral = pd.concat((df_01, df_02, df_03))



class TestSetAnabolizantes(unittest.TestCase):
    """
    a classe vai conter os diferentes testes feitos para a função
    """

    def test_dataframe_esperado(self):
        """
        verifica se a função consegue lidar com os dataframes esperados

        Obs.: fica difícil comparar dataframes sem usar a função, por isso o teste
        verifica se ela retorna um dataframe mesmo se recebe o parâmetro esperado
        """
        self.assertIsInstance(set_anabolizantes(dataframe_geral), pd.core.frame.DataFrame)

    def test_dataframe_vazio(self):
        """
        verifica se a função consegue lidar com um dataframe vazio
        """
        self.assertEqual(set_anabolizantes(pd.DataFrame), None)

    def test_string(self):
        """
        verifica se a função consegue lidar quando é passada uma string
        """
        self.assertEqual(set_anabolizantes("Matheus"), None)

    def test_float(self):
        """
        verifica se a função consegue lidar quando é passado um float
        """
        self.assertEqual(set_anabolizantes(3.14156592), None)

    def test_bool(self):
        """
        verifica se a função consegue lidar quando é passado um booleano
        """
        self.assertEqual(set_anabolizantes(True), None)

    def test_list(self):
        """
        verifica se a função consegue lidar quando é passada uma lista de valores
        """
        self.assertEqual(set_anabolizantes(["Matheus", "Sillas", "Luciano", "Leonardo"]), None)


if __name__ == "__main__":
    unittest.main()