import sys, os
esse_caminho = os.path.dirname(os.path.abspath(__file__))
sys.path.append(esse_caminho)

import pandas as pd
import utils
import matplotlib.pyplot as plt
import doctest
from typing import Literal, Iterable, Optional
from numpy import datetime64


def filtra_e_contatena(coluna_do_valor: str, valores_procurados: list | str) -> pd.DataFrame:
    '''Usa as funções do módulo utils para concatenar todas as datas disponíveis e pegar apenas as linhas com os valores procurados

    Parâmetros:
    ------------
    coluna_do_valor:
        Tipo: str 
        Descrição: 
            nome da coluna em que o valor procurado deve estar

    valores_procurados: 
        Tipo: list | str
        Descrição: 
            valor, caso string, ou valores, caso lista, que serão procurados na coluna
    
    Retorna:
    ---------
    dataframe:
        Tipo: pandas.DataFrame
        Descrição: dataframe pandas com os dados filtrados
    
    '''
    dataframe = utils.concat_data_by_dates(f"2014/01", f"2014/12")
    dataframe = utils.filtra_dados_por_valores_procurados(dataframe, coluna_do_valor, valores_procurados)
    for year in range(2014, 2021+1):
        novo_dataframe = utils.concat_data_by_dates(f"{year}/01", f"{year}/12")
        novo_dataframe = utils.filtra_dados_por_valores_procurados(novo_dataframe, coluna_do_valor, valores_procurados)
        dataframe = pd.concat((dataframe, novo_dataframe))
    
    return dataframe

def cria_datetime(dataframe: pd.DataFrame) -> pd.Series:
    '''
    Cria uma série do Pandas com datetimes relativos aos anos e meses das colunas "ANO_VENDA" e "MES_VENDA".
    Os dias no datetime serão todos o primeiro dia de cada mês.

    Parâmetros:
    -------------
    dataframe: 
        Tipo: pandas.DataFrame
        Descrição:
            o dataframe do Pandas com as colunas "ANO_VENDA" e "MES_VENDA".

    Retorna:
    ---------
    datetimes: 
        Tipo: pandas.Series
        Descrição: série do Pandas com as datas em formato datetime.
    
    Exemplo:
    ---------
    >>> cria_datetime(pd.DataFrame({"ANO_VENDA": [2020, 2020, 2021], "MES_VENDA": [3, 3, 12]}))
    0   2020-03-01
    1   2020-03-01
    2   2021-12-01
    dtype: datetime64[ns]
    '''
    datetimes = {"Year": dataframe["ANO_VENDA"],
                "Month": dataframe["MES_VENDA"],
                "Day": ["1"]*len(dataframe.index)}
    
    return pd.to_datetime(datetimes)

def regiao_estado(sigla_estado: str) -> str:
    """
    Retorna a região do estado brasileiro: Norte, Nordeste, Centro-Oeste, Sudeste ou Sul.
    
    Parâmetros
    -------------
    sigla_estado:
        Tipo: str
        Descrição: 
            Sigla do estado brasileiro
        Exemplo: "MG"
    
    Retorna:
    --------
    regiao:
        Tipo: str | None
        Descrição: 
            Região em que o estado brasileiro está. 
            Se a sigla inserida for inexistente, retorna None.
        Exemplo: Sudeste
    
    Exemplos
    ----------
    >>> regiao_estado("RR")
    'Norte'

    >>> regiao_estado("BH")
    
    """

    estados = {
        "AC": "Norte",
        "AP": "Norte",
        "AM": "Norte",
        "PA": "Norte",
        "RO": "Norte",
        "RR": "Norte",
        "TO": "Norte",
        "MA": "Nordeste",
        "PI": "Nordeste",
        "CE": "Nordeste",
        "RN": "Nordeste",
        "PB": "Nordeste",
        "PE": "Nordeste",
        "AL": "Nordeste",
        "SE": "Nordeste",
        "BA": "Nordeste",
        "GO": "Centro-Oeste",
        "MT": "Centro-Oeste",
        "MS": "Centro-Oeste",
        "DF": "Centro-Oeste",
        "SP": "Sudeste",
        "MG": "Sudeste",
        "RJ": "Sudeste",
        "ES": "Sudeste",
        "PR": "Sul",
        "SC": "Sul",
        "RS": "Sul"
    }
    try:
        regiao = estados[sigla_estado]
    except KeyError:
        return None
    
    return regiao

def grafico_linhas(datas: Iterable[datetime64], valores: tuple[Iterable] | Iterable, labels: tuple[str] | str, titulo: str | None = None, transparencias: tuple[float] | float = 1.0):
    """Prepara um gráfico de linhas com os dados fornecidos usando o matplotlib.pyplot
    
    Parâmetros
    -------------
    datas:
        Tipo: Iterable[datetime]
        Descrição: 
            Datas que serão usadas no eixo X.
    
    valores:
        Tipo: tuple[Iterable] | Iterable
        Descrição: 
            Valores que serão plotados em relação ao eixo Y. 
            Se há mais de uma linha, o parâmetro deve receber uma tupla com os dados de cada linha.
    
    labels:
        Tipo: tuple[str] | str
        Descrição:
            Legendas das linhas a serem plotadas. 
            Se há mais de uma linha, esse parâmetro deve receber uma tupla.
    
    titulo:
        Tipo: str | None
        Descrição:
            Título do gráfico.
    
    transparencias:
        Tipo: tuple[float] | float
        Descrição:
            Transparências das linhas a serem geradas. 
            Se há mais de uma linha, esse parâmetro deve receber uma tupla.
    
    Exemplo:
    ---------
    >>> datas = cria_datetime(pd.DataFrame({"ANO_VENDA": [2020, 2020, 2021], "MES_VENDA": [3, 3, 12]}))
    >>> grafico_linhas(datas, ([1, 3, 4], [2, 3, 1]), ("Primeira linha"))
    Traceback (most recent call last):
    ...
    ValueError: As quantidades de valores e labels são diferentes.
    """

    if type(valores) != tuple:
        valores = tuple([valores])
    if type(labels) != tuple:
        labels = tuple([labels])
    
    if len(labels) != len(valores):
        raise ValueError("As quantidades de valores e labels são diferentes.")
    
    if type(transparencias) == float or type(transparencias) == int:
        transparencias = [transparencias]*len(valores)
    
    if len(transparencias) != len(valores):
        raise ValueError("Tuples of different sizes given.")

    for i in range(len(valores)):
        plt.plot(datas, valores[i], alpha = transparencias[i], label = labels[i])

    plt.legend(loc='best')
    plt.suptitle(titulo)

def contagem_elementos(dataframe: pd.DataFrame, elemento_contado: str, nome_da_serie: str) -> pd.Series:
    """
    Retorna uma série do Pandas com as contagens dos elementos na ordem deles.
    
    Parâmetros
    -------------
    dataframe:
        Tipo: pandas.DataFrame
        Descrição: 
            DataFrame a ser modificado

    elemento_contado:
        Tipo: str
        Descrição: 
            Nome da coluna em que o value_counts vai ser feito
    
    nome_da_serie:
        Tipo: str
        Descrição: 
            nome da série a ser retornada
    
    Retorna
    --------
    contagem:
        Tipo: pandas.Series
        Descrição: 
            série do pandas com as informações feitas
    
    Exemplos
    --------
    >>> contagem_elementos(pd.DataFrame({"NOME": ["A", "B", "B"]}), "NOME", "SERIE EXEMPLO")
    NOME
    A    1
    B    2
    Name: SERIE EXEMPLO, dtype: int64

    """

    dataframe = dataframe.copy() # Para não alterar o dataframe original

    dataframe.sort_values(elemento_contado)
    contagem = dataframe.value_counts(elemento_contado, sort=False).rename(nome_da_serie)

    return contagem

def luciano_vis(acao: Literal["show", "save", None], path: str|None = None):
    """
    Gera o gráfico escolhido por Luciano. Vai ser exibido ou salvo.

    Parâmetros:
    ------------
    acao:
        Tipo: str | None
        Descrição: 
            Ação a ser executada depois de formar o gráfico. Pode ser:
            "show": irá mostrar o gráfico e fechar a figura.
            "save": irá salvar o gráfico e fechar a figura.
            None: formará o gráfico, mas não o fechará.
    
    path:
        Tipo: str | None
        Descrição: 
            path em que a figura será salva. É necessário caso o parâmetro acao seja "save".
    
    Exemplo:
    -----------
    >>> luciano_vis(acao = "salvar")
    Traceback (most recent call last):
    ...
    ValueError: Ação 'salvar' inválida. 
    Valores válidos: 'show', 'save', None

    """


    if acao not in ["show", "save", None]:
        raise ValueError(f"Ação '{acao}' inválida. \nValores válidos: 'show', 'save', None")
    
    if acao == "save" and type(path) != str:
        raise ValueError(f"Especifique um caminho para salvar o arquivo.")

    principios_de_antidepressivos = ["SELEGILINA","SERTRALINA", "AMITRIPTILINA", "CITALOPRAM",
                                     "CLOMIPRAMINA", "IPRONIAZIDA", "MOCLOBEMIDA", "IMIPRAMINA",
                                     "TRIMIPRAMINA", "NORTRIPTILINA", "PROTRIPTILINA", "DOXEPINA",
                                     "AMOXAPINA", "DOTIEPINA", "OUDOSULEPINA", "FLUOXETINA",
                                     "FLUVOXAMINA", "PAROXETINA", "ESCITALOPRAM", "NORCITALOPRAM",
                                     "TIANEPTINA", "MIANSERINA", "DULOXETINA", "MIRTAZAPINA", "MAPROTILINA", 
                                     "NEFAZODONA", "MILNACIPRANA", "TRAZODONA", "DESVENLAFAXINA", "VENLAFAXINA",
                                     "BUPROPIONA"]
    
    try:
        dataframe_antidepressivos = pd.read_csv("dados/Manipulados_ANTIDEPRESSIVOS.csv")
    except:
        dataframe_antidepressivos = filtra_e_contatena("PRINCIPIO_ATIVO", principios_de_antidepressivos)
        dataframe_antidepressivos.to_csv("dados/Manipulados_ANTIDEPRESSIVOS.csv", index=False)

    dataframe_antidepressivos["DATA"] = cria_datetime(dataframe_antidepressivos)
    dataframe_antidepressivos["REGIAO"] = dataframe_antidepressivos["UF_VENDA"].apply(regiao_estado)
    antidepressivos_norte = utils.filtra_dados_por_valores_procurados(dataframe_antidepressivos, "REGIAO", "Norte")
    antidepressivos_nordeste = utils.filtra_dados_por_valores_procurados(dataframe_antidepressivos, "REGIAO", "Nordeste")
    antidepressivos_centroeste = utils.filtra_dados_por_valores_procurados(dataframe_antidepressivos, "REGIAO", "Centro-Oeste")
    antidepressivos_sudeste = utils.filtra_dados_por_valores_procurados(dataframe_antidepressivos, "REGIAO", "Sudeste")
    antidepressivos_sul = utils.filtra_dados_por_valores_procurados(dataframe_antidepressivos, "REGIAO", "Sul")

    
    contagem_norte = contagem_elementos(antidepressivos_norte, "DATA", "NORTE")
    contagem_nordeste = contagem_elementos(antidepressivos_nordeste, "DATA", "NORDESTE")
    contagem_centroeste = contagem_elementos(antidepressivos_centroeste, "DATA", "CENTRO-OESTE")
    contagem_sudeste = contagem_elementos(antidepressivos_sudeste, "DATA", "SUDESTE")
    contagem_sul = contagem_elementos(antidepressivos_sul, "DATA", "SUL")

    contagem = pd.concat([contagem_norte, contagem_nordeste, contagem_centroeste, contagem_sudeste, contagem_sul], axis=1)
    contagem.fillna(0, inplace=True)

    grafico_linhas(contagem.index, (contagem["NORTE"], 
                                    contagem["NORDESTE"], 
                                    contagem["CENTRO-OESTE"], 
                                    contagem["SUDESTE"],
                                    contagem["SUL"]), 
                                    tuple(contagem.columns), titulo = "ANTIDEPRESSIVOS POR REGIÃO")
    if acao == "show":
        plt.show()
        plt.close()
    elif acao == "save":
        plt.savefig(path)
        plt.close()



if __name__ == "__main__":
    luciano_vis("show")
    doctest.testmod(verbose=True)
    