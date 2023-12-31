"""
Módulo para a criação da visualização do integrante Leonardo. 
As funções desse módulo são utilizadas para a análise exploratória da base de dados e a elaboração da
visualização baseada nas vendas anuais do remédio Hemitartarato de Zolpidem.
"""

import sys, os
esse_caminho = os.path.dirname(os.path.abspath(__file__))
sys.path.append(esse_caminho)

import pandas as pd 
import matplotlib.pyplot as plt 
import utils 
import doctest

def dataframe_de_zolpidem(dataframe_selecionado: pd.DataFrame) -> pd.DataFrame:
    """
    A função recebe um dataframe que contém registros de venda do Hemitartarato de Zolpidem dentro de um intervalo
    de tempo e retorna um dataframe que contém a quantidade de vendas do remédio por ano.

    Parameters
    ----------
    dataframe_selecionado: pd.DataFrame
        Dataframe referente ao remédio Zolpidem.

    Returns
    ----------
    df_venda_por_ano: pd.DataFrame
        Dataframe das quantidades vendidas por ano. 

    Examples
    ----------
    # >>> dataframe_de_zolpidem(utils.concat_data_by_dates("2014/01", "2020/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"]))

    Tests
    ----------
    >>> dataframe_de_zolpidem(2023)
    Parâmetro inválido.

    >>> dataframe_de_zolpidem(pd.DataFrame())  
    O dataframe não contém a coluna PRINCIPIO_ATIVO.

    """

    # Validação do dataframe
    try:
        if type(dataframe_selecionado) != pd.DataFrame:
            raise TypeError
    except TypeError:
        print("Parâmetro inválido.")     

    else:
        try:
            df_hemitartarato_de_zolpidem = (dataframe_selecionado[dataframe_selecionado["PRINCIPIO_ATIVO"] == "HEMITARTARATO DE ZOLPIDEM"]).reset_index(drop=True)
            df_zolpidem = (dataframe_selecionado[dataframe_selecionado["PRINCIPIO_ATIVO"] == "ZOLPIDEM"]).reset_index(drop=True)

        except KeyError:
            print("O dataframe não contém a coluna PRINCIPIO_ATIVO.") 
        except BaseException as err:
             print("Outro erro encontrado!", err) 

        else:
            # Gerando o dataframe que contém apenas o Zolpidem

            df = pd.concat([df_hemitartarato_de_zolpidem, df_zolpidem]).reset_index()

            # Contagem por ano

            df["REMÉDIO_VENDIDO"] = df["PRINCIPIO_ATIVO"].replace({"HEMITARTARATO DE ZOLPIDEM": 1, "ZOLPIDEM": 1})

            df_venda_por_ano = df.groupby("ANO_VENDA")["REMÉDIO_VENDIDO"].sum().sort_values(ascending = False).reset_index()

            return df_venda_por_ano

def visualizacao_leonardo(dataframe_de_vendas_anuais: pd.DataFrame, caminho_pasta: str) -> pd.DataFrame:
    """
    A função recebe um dataframe que possui a quantidade de vendas do remédio Zolpidem por ano e retorna
    um gráfico de linhas baseado no dataframe.

    Parameters
    ----------
    dataframe_de_vendas_anuais: pd.DataFrame
        Dataframe que contém o total de vendas anuais do remédio Hemitartarato de Zolpidem.
    
    caminho_pasta: str
        Caminho da pasta onde o arquivo de imagem da visualização será salvo.

    Returns
    -------
    "Visualização finalizada": str
        Mensagem de conclusão da visualização.

    """

    df_venda_por_ano = dataframe_de_zolpidem(dataframe_de_vendas_anuais)  
    
    # Construção do gráfico

    plt.scatter(df_venda_por_ano["ANO_VENDA"], df_venda_por_ano["REMÉDIO_VENDIDO"], marker="*", c = "Black")
    plt.plot(df_venda_por_ano["ANO_VENDA"], df_venda_por_ano["REMÉDIO_VENDIDO"], c = "Gray")
    plt.suptitle("Venda de Zolpidem ao Longo dos Anos", fontweight = "bold")
    plt.xlabel("Anos", fontweight = "bold")
    plt.ylabel("Vendas", fontweight = "bold")
    plt.gca().set_facecolor("Beige")

    plt.savefig(f"{caminho_pasta}\zolpidem.png")

    plt.show()

    return "Visualização finalizada!"

if __name__ == "__main__":
    doctest.testmod(verbose = True)    