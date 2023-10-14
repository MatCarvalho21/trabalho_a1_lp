import pandas as pd
import utils
import matplotlib.pyplot as plt

def filtra_e_contatena(coluna_do_valor: str, valores_procurados: list or str):
    '''Usa as funções do módulo utils para concatenar todas as datas disponíveis e pegar apenas as linhas com os valores procurados

    Parâmetros:
        coluna_do_valor (str): nome da coluna em que o valor procurado deve estar
        valores_procurados (list or str): valor, caso string, ou valores, caso lista, que serão procurados na coluna
    
    Retorna:
        dataframe (pandas.DataFrame): dataframe pandas com os dados filtrados
    
    '''
    dataframe = utils.concat_data_by_dates(f"2014/01", f"2014/12")
    dataframe = utils.filtra_dados_por_valores_procurados(dataframe, coluna_do_valor, valores_procurados)
    for year in range(2014, 2021+1):
        novo_dataframe = utils.concat_data_by_dates(f"{year}/01", f"{year}/12")
        novo_dataframe = utils.filtra_dados_por_valores_procurados(novo_dataframe, coluna_do_valor, valores_procurados)
        dataframe = pd.concat((dataframe, novo_dataframe))
    
    return dataframe

def cria_datetime(dataframe: pd.DataFrame):
    '''
    Cria uma série do Pandas com datetimes relativos aos anos e meses das colunas "ANO_VENDA" e "MES_VENDA".
    Os dias no datetime serão todos o primeiro dia de cada mês.

    Parâmetros:
        dataframe (pd.Dataframe): o dataframe do Pandas com as colunas "ANO_VENDA" e "MES_VENDA".

    Retorna:
        datetimes (pd.Series): série do Pandas com as datas em formato datetime.
    '''
    datetimes = {"Year": dataframe["ANO_VENDA"],
                 "Month": dataframe["MES_VENDA"],
                 "Day": ["1"]*len(dataframe.index)}
    
    return pd.to_datetime(datetimes)

def grafico_linhas(datas, valores: float or int):
    """Prepara um gráfico de linhas com os dados fornecidos usando o matplotlib.pyplot"""
    plt.plot(datas, valores)
    plt.show()

if __name__ == "__main__":
    
    try:
        dataframe = pd.read_csv("dados/Manipulados_METILFENIDATO.csv", decimal=",")
    except:
        dataframe = filtra_e_contatena("PRINCIPIO_ATIVO", "CLORIDRATO DE METILFENIDATO")
        dataframe.to_csv("dados/Manipulados_METILFENIDATO.csv", index=False)
    
    dataframe["DATA"] = cria_datetime(dataframe)
    dataframe.sort_values(by="DATA")
    print(type(cria_datetime(dataframe)))
    #grouped_dataframe = dataframe.groupby(["DATA"]).value_counts()
    '''grouped_dataframe = dataframe.value_counts("DATA", sort = False)
    print(grouped_dataframe)
    grafico_linhas(grouped_dataframe.index, grouped_dataframe)
    '''

    
    