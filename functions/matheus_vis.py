import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np 
import doctest
from dados_anabolizantes import set_anabolizantes

"""Esse módulo conta com três funções. Todas elas estão ligadas à contrução da visualização sobre a evolução
no uso de anabolizantes. A função contida nesse módulo vai ter como objetivo gerar os frames que serão
usados para contruir a visualização final."""

# dataframes para teste
df_01 = pd.read_csv("dados\Manipulados_2014_01.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_02 = pd.read_csv("dados\Manipulados_2014_02.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
df_03 = pd.read_csv("dados\Manipulados_2014_03.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
dataframe_geral = pd.concat((df_01, df_02, df_03))
dataframe_teste = set_anabolizantes(dataframe_geral)

dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Idade': [25, 30, 22, 35, 28],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}
dataframe_invalido = pd.DataFrame(dados)

lista_de_colunas = ['ANO_VENDA',
                    'MES_VENDA', 
                    'UF_VENDA', 
                    'MUNICIPIO_VENDA', 
                    'DCB', 
                    'PRINCIPIO_ATIVO', 
                    'QTD_ATIVO_POR_UNID_FARMACOTEC', 
                    'UNIDADE_MEDIDA_PRINCIPIO_ATIVO', 
                    'QTD_UNIDADE_FARMACOTECNICA', 
                    'TIPO_UNIDADE_FARMACOTECNICA', 
                    'CONSELHO_PRESCRITOR', 
                    'UF_CONSELHO_PRESCRITOR', 
                    'TIPO_RECEITUARIO', 
                    'CID10', 
                    'SEXO', 
                    'IDADE', 
                    'UNIDADE_IDADE']

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

def gerador_de_frames(dataframe_filtrado:pd.DataFrame, ano_analizado:int, mes_analizado:int) -> str:
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
    >>> gerador_de_frames("Matheus", 2014, 5)
    'Não foi fornecido um dataframe.'

    >>> gerador_de_frames(pd.DataFrame(), 2014, 5)
    'O dataframe está vazio.'

    >>> gerador_de_frames(dataframe_invalido, 2014, 5)
    'O dataframe fornecido está em um formato inválido'

    >>> gerador_de_frames(dataframe_teste, "matheus", 5)
    'O ano fornecido deve ser um inteiro.'

    >>> gerador_de_frames(dataframe_teste, 2015, "matheus")
    'O mês fornecido deve ser um inteiro'
    """

    try:
        dataframe_filtrado = pd.DataFrame(dataframe_filtrado)
    except ValueError:
        return "Não foi fornecido um dataframe."
    
    try: 
        if dataframe_filtrado.shape == (0,0):
            raise AttributeError
    except AttributeError:
        return "O dataframe está vazio."

    try:
        if list(dataframe_filtrado.columns) != lista_de_colunas:
            raise AttributeError
    except AttributeError:
        return "O dataframe fornecido está em um formato inválido"

    try:
        ano_analizado = int(ano_analizado)
    except ValueError:
        return "O ano fornecido deve ser um inteiro."
    
    try:
        mes_analizado = int(mes_analizado)
    except ValueError:
        return "O mês fornecido deve ser um inteiro"
        

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
    grafico1.set_ylim(bottom=0, top=30000)
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
    grafico2.set_ylim(bottom=0, top=3000)
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
    grafico3.set_ylim(bottom=0, top=300)
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

    return "Deu tudo certo!"

if __name__ == "__main__":
    doctest.testmod()