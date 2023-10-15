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
    df_venda_por_ano: pd.Dataframe
        Dataframe das quantidades vendidas por ano. 

    Examples
    ----------
    >>> dataframe_de_zolpidem(utils.concat_data_by_dates("2014/01", "2020/12", filtered_columns = ["ANO_VENDA", "PRINCIPIO_ATIVO"]))

    >>> dataframe_de_zolpidem(2023)
    O dataframe é inválido. 

    >>> dataframe_de_zolpidem(pd.Dataframe())  
    O dataframe está vazio. 

    """

    try:
        df_hemitartarato_de_zolpidem = (dataframe_selecionado[dataframe_selecionado["PRINCIPIO_ATIVO"] == "HEMITARTARATO DE ZOLPIDEM"]).reset_index(drop=True)
        df_zolpidem = (dataframe_selecionado[dataframe_selecionado["PRINCIPIO_ATIVO"] == "ZOLPIDEM"]).reset_index(drop=True)
    except KeyError:
        print("O dataframe não contém a coluna PRINCIPIO_ATIVO.")  

    # Gerando o dataframe que contém apenas o Zolpidem

    df = pd.concat([df_hemitartarato_de_zolpidem, df_zolpidem]).reset_index()

    # Contagem por ano

    df["REMÉDIO_VENDIDO"] = df["PRINCIPIO_ATIVO"].replace({"HEMITARTARATO DE ZOLPIDEM": 1, "ZOLPIDEM": 1})

    df_venda_por_ano = df.groupby("ANO_VENDA")["REMÉDIO_VENDIDO"].sum().sort_values(ascending = False).reset_index()

    return df_venda_por_ano

def visualizacao_leonardo(dataframe_de_vendas_anuais: pd.DataFrame) -> pd.DataFrame:
    """
    A função recebe um dataframe que possui a quantidade de vendas do remédio Zolpidem por ano e retorna
    um gráfico de linhas baseado no dataframe.

    Parameters
    ----------
    dataframe_de_vendas_anuais: pd.DataFrame
        Dataframe que contém o total de vendas anuais do remédio Hemitartarato de Zolpidem.

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

    plt.savefig("functions\Leonardo_imagem\\zolpidem.png")

    plt.show()

    return "Visualização finalizada"

if __name__ == "__main__":
    doctest.testmod(verbose = True)  