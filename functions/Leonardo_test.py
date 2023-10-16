import unittest
import Leonardo_vis 
import utils
import pandas as pd

dataframe_selecionado = utils.concat_data_by_dates("2014/01", "2016/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"])

class TestDataFrameDeZolpidem(unittest.TestCase):
    def test_type_dataframe(self):
        self.assertIsInstance(Leonardo_vis.dataframe_de_zolpidem(dataframe_selecionado), pd.DataFrame)

class TestVisualizacao(unittest.TestCase):
    
    def test_visualizacao_leonardo(self):
        self.assertEqual(Leonardo_vis.visualizacao_leonardo(dataframe_selecionado), "Visualização finalizada!")

if __name__ == '__main__':
    unittest.main()