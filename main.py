import sys
import os

esse_caminho = os.path.dirname(os.path.abspath(__file__))
caminho_functions = os.path.join(esse_caminho, "functions")
sys.path.append(caminho_functions)

import pandas as pd
from utils import concat_data_by_dates, filtra_dados_por_valores_procurados, set_anabolizantes
from matheus_vis import gerador_de_frames, save_frames
from sillas_vis import visualizacao_sillas
from gifs import seletor_de_frames, gerador_de_gif
from Leonardo_vis import visualizacao_leonardo, dataframe_de_zolpidem
from luciano_vis import luciano_vis

visualizacao_sillas("2020/01", "2021/11", "functions\\sillas_imagens")
lista_de_frames_sillas = seletor_de_frames(2020, 2021, "functions\sillas_imagens")
gerador_de_gif(lista_de_frames_sillas, "assets\\visualizacoes_finais", "vis_final_sillas", 1)

for cada_ano in range(2014, 2021):
    dados_brutos = concat_data_by_dates(f"{cada_ano}/01", f"{cada_ano}/12")
    dados_filtrados = set_anabolizantes(dados_brutos) 
    for cada_mes in range(1, 13):
        figure, valor_nulo = gerador_de_frames(dados_filtrados, str(cada_ano), str(cada_mes))
        save_frames(figure, cada_ano, cada_mes, "functions\\matheus_imagens")
lista_de_frames_sillas = seletor_de_frames(2014, 2020, "functions\matheus_imagens")
gerador_de_gif(lista_de_frames_sillas, "assets\\visualizacoes_finais", "vis_final_matheus", 3)

dados_leo = concat_data_by_dates("2014/01", "2020/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"])
visualizacao_leonardo(dados_leo, "assets\\visualizacoes_finais")

luciano_vis("save", "assets/visualizacoes_finais/vis_luciano.png")