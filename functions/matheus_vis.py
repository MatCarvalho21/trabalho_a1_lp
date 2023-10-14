import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np 
import doctest
import imageio

lista_de_anabolizantes = ["TESTOSTERONA",
                            "ESTANOZOLOL",
                            "NANDROLONA"]

x_meses = {"Janeiro": 1,
            "Fevereiro": 2,
            "Março": 3,
            "Abril": 4,
            "Maio": 5,
            "Junho": 6,
            "Julho": 7,
            "Agosto": 8,
            "Setembro": 9,
            "Outubro": 10,
            "Novembro": 11,
            "Dezembro": 12}

def grafico_animado(dataframe_filtrado:pd.DataFrame, ano_analizado:int, mes_analizado:int) -> None:
    """
    A função tem como objetivo criar vários frames, separados por ano e por mês, 
    para que eles sejam usados em um gráfico animado. Ela vai gerar várias imagens
    que serão utilizadas para montar a visualização animada.

    Parameters
    ----------
    dataframe_filtrado
        type: pd.DataFrame
        description: o dataframe filtrado e concatenado que vai ser base da análise
    
    ano_analizado
        type: int
        description: o número do mês que vamos plotar 
        example: 2015

    mes_analizado
        type: int
        description: o número do ano que vamos plotar
        example: 5

    Test
    ----------

    """

    # filtragem e configuração do dataframe
    dataframe_filtrado["NUMERO_DE_VENDAS"] = 1
    dataframe_filtrado = dataframe_filtrado[dataframe_filtrado["ANO_VENDA"] == ano_analizado]
    dataframe_filtrado = dataframe_filtrado[dataframe_filtrado["MES_VENDA"] <= mes_analizado]

    # criação dos objetos de plotagem
    figure, (grafico1, grafico2, grafico3) = plt.subplots(nrows=1, 
                                    ncols=3, 
                                    sharex=True, 
                                    figsize=(20, 5))
    
    #TESTOSTERONA #######################################################################################################

    # plotagem do gráfico 1
    df_testosterona = dataframe_filtrado[dataframe_filtrado["PRINCIPIO_ATIVO"] == "TESTOSTERONA"].reset_index(drop=True)
    df_testosterona = df_testosterona[["MES_VENDA", "NUMERO_DE_VENDAS"]]
    df_testosterona = df_testosterona.groupby("MES_VENDA").sum().reset_index(drop=True)
    numero_vendas_testosterona = list(df_testosterona["NUMERO_DE_VENDAS"]) 

    grafico1.plot(list(x_meses.values())[0:mes_analizado], numero_vendas_testosterona, color="midnightblue")
    grafico1.scatter(list(x_meses.values())[0:mes_analizado], numero_vendas_testosterona, color="midnightblue")
    grafico1.set_ylim(bottom=0, top=15000)
    grafico1.axhline(y=np.nanmean(numero_vendas_testosterona), color="red", linestyle='--', linewidth=1.5, label='Média')
    grafico1.legend()
    grafico1.set_title("Testosterona")
    grafico1.set_ylabel('Nº de Vendas', fontsize=12)

    #ESTANOZOLOL ########################################################################################################

    # plotagem do gráfico 2
    df_estanozolol = dataframe_filtrado[dataframe_filtrado["PRINCIPIO_ATIVO"] == "ESTANOZOLOL"].reset_index(drop=True)
    df_estanozolol = df_estanozolol[["MES_VENDA", "NUMERO_DE_VENDAS"]]
    df_estanozolol = df_estanozolol.groupby("MES_VENDA").sum().reset_index(drop=True)
    numero_vendas_estanozolol = list(df_estanozolol["NUMERO_DE_VENDAS"]) 

    grafico2.plot(list(x_meses.values())[0:mes_analizado], numero_vendas_estanozolol, color="midnightblue")
    grafico2.scatter(list(x_meses.values())[0:mes_analizado], numero_vendas_estanozolol, color="midnightblue")
    grafico2.set_ylim(bottom=0, top=1500)
    grafico2.axhline(y=np.nanmean(numero_vendas_estanozolol), color="red", linestyle='--', linewidth=1.5, label='Média')
    grafico2.legend()
    grafico2.set_title("Estanozolol")
    grafico2.set_xlabel('Meses do Ano', fontsize=12)

    #NANDROLONA ########################################################################################################

    # plotagem do gráfico 3
    df_nandrolona = dataframe_filtrado[dataframe_filtrado["PRINCIPIO_ATIVO"] == "NANDROLONA"].reset_index(drop=True)
    df_nandrolona = df_nandrolona[["MES_VENDA", "NUMERO_DE_VENDAS"]]
    df_nandrolona = df_nandrolona.groupby("MES_VENDA").sum().reset_index(drop=True)
    numero_vendas_nandrolona = list(df_nandrolona["NUMERO_DE_VENDAS"]) 

    grafico3.plot(list(x_meses.values())[0:mes_analizado], numero_vendas_nandrolona, color="midnightblue")
    grafico3.scatter(list(x_meses.values())[0:mes_analizado], numero_vendas_nandrolona, color="midnightblue")
    grafico3.set_ylim(bottom=0, top=150)
    grafico3.axhline(y=np.nanmean(numero_vendas_nandrolona), color="red", linestyle='--', linewidth=1.5, label='Média')
    grafico3.legend()
    grafico3.set_title("Nandrolona")

    ####################################################################################################################

    plt.suptitle(f"Venda de Anabolizantes Por Ano ({ano_analizado})", fontsize=18)
    plt.xlim(0, 13)

    # salvando as imagens
    plt.savefig(f'functions\matheus_imagens\\frame_{ano_analizado}_{mes_analizado}.png', 
                transparent = False,  
                facecolor = 'white'
               )
    
    plt.close()
    
    # confirmação do processo
    print(f"{ano_analizado}, {mes_analizado} concluido")

def animacao_do_grafico(data_inicial:str, data_final:str, path_pasta_imagens:str) -> list:
    """
    A função recebe a data_inicial e a data_final, elas criam uma range de imagens, além disso 
    o path relativo da pasta que contém as imagens em questão. Ela, então, cria uma lista com 
    as imagens e a retorna para que possam ser concatenadas em um gif. 

    Parameters
    ----------
    data_inicial
        type: str
        description: inicio da range de datas 
        example: "2020"

    data_final
        type: str
        description: final da range de datas
        example: "2021"

    path_pasta_imagens
        type: str
        description: 
        example: "root\\folder_01\\final_folder"

    Return
    ----------
    lista_de_frames
        type: list
        description: lista com as imagens que irão compor o gif da visualização 


    Test
    ----------
    """

    lista_de_frames = list()

    for cada_ano in range(int(data_inicial), int(data_final) + 1):
        for cada_mes in range(1, 13):
            frame = imageio.v2.imread(f"{path_pasta_imagens}\\frame_{cada_ano}_{cada_mes}.png")
            lista_de_frames.append(frame)

    return lista_de_frames

print(animacao_do_grafico("2014", "2016", "functions\matheus_imagens"))

    
if __name__ == "__main__":
    pass