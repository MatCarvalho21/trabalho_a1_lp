import pandas as pd   
from dados_anabolizantes import set_anabolizantes
from matheus_vis import gerador_de_frames, seletor_de_frames, gerador_de_gif

lista_de_dataframes = list()

for cada_ano in range(2014, 2021):
    for cada_mes in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        dataframe_auxiliar = pd.read_csv(f"dados\Manipulados_{cada_ano}_{cada_mes}.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
        lista_de_dataframes.append(set_anabolizantes(dataframe_auxiliar))
        print(f"{cada_ano}-{cada_mes} deu certo!")

dataframe_final = pd.concat(lista_de_dataframes).reset_index(drop=True)
print("FINAL CORRETO")

for cada_ano in range(2014, 2021):
    for cada_mes in range(1, 13):
        gerador_de_frames(dataframe_final, cada_ano, cada_mes)
        print(f"{cada_ano}-{cada_mes} deu certo!")

lista_de_frames = seletor_de_frames("2014", "2020", "functions\matheus_imagens")
gerador_de_gif(lista_de_frames, "functions\matheus_imagens", "resultado.gif")