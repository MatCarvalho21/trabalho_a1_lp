import geobr
import pandas as pd
import matplotlib.pyplot as plt
import doctest
import utils
from get_data import get_dates_between_dates


def soma_vendas_por_atributo(dados:pd.DataFrame, atributo:str) -> pd.DataFrame:
    """Função que soma algum atributo de um dataframe.

    Recebe um dataframe e retorna um dataframe contendo o atributo selecionado e a quantidade
    de observações em uma coluna chamada "vendas".

    Parameters
    ----------
    dados : pd.DataFrame
        Dataframe com a coluna do atributo
    atributo : str
        atributo onde as observações serão somadas. 

    Returns
    -------
    pd.DataFrame
        Dataframe que contém como colunas o atributo e "vendas", sendo as vendas
        a soma da quantidade de observações do atributo.

    Raises
    ------
    TypeError
        Tipo incorreto do dataframe ou do atributo
    ValueError
        Coluna do atributo não está na base de dados
    
    Test
    ----------
    >>> dados = pd.DataFrame({'PINCIPIO_ATIVO': ['CLOROQUINA', 'DIFOSFATO DE CLOROQUINA', 'HIDROXICLOROQUINA', 'CLOROQUINA'], 'UF': ["SP", "RJ", "RJ", "MS"]})
    >>> soma_vendas_por_atributo(dados, "UF")
       UF  vendas
    0  RJ       2
    1  MS       1
    2  SP       1

    >>> soma_vendas_por_atributo(66, "UF")
    Dataframe ou atributo inválido, tente inserir outro dataframe ou um atributo como string.

    >>> soma_vendas_por_atributo(dados, 66)
    Dataframe ou atributo inválido, tente inserir outro dataframe ou um atributo como string.

    >>> soma_vendas_por_atributo(dados, "COLUNA_INVÁLIDA")
    Atributo inválido, insira uma coluna da base de dados.
    """
    # Valida a base de dados e o tipo do atributo
    try:
        if type(dados) != pd.DataFrame or type(atributo) != str:
            raise TypeError
    
    except TypeError:
        print("Dataframe ou atributo inválido, tente inserir outro dataframe ou um atributo como string.")
    
    else:
        # Valida o atributo
        try:
            if atributo not in dados.columns:
                raise ValueError
        except ValueError:
            print("Atributo inválido, insira uma coluna da base de dados.")
        else:
            # Faz a contagem de observações.
            soma_vendas = pd.DataFrame()
            vendas_totais = dados.value_counts(atributo)

            soma_vendas[atributo] = vendas_totais.index
            soma_vendas["vendas"] = vendas_totais.values

            return soma_vendas


def mapeia_dados_estaduais(dados_mapeamento:pd.DataFrame, coluna_estados:str,) -> pd.DataFrame:
    """Função que une um dataframe desejado aos dados relacionados ao formato dos estados brasileiros da biblioteca geobr

    A blblioteca geobr disponibiliza o formato dos estados brasileiros que auxiliam na plotagem do matplotlib,
    esta função apenas une a base de dados desejada à base do geobr, para isto, a base de dados desejada deve conter
    uma coluna com a silga dos estados, ex: "SP", "RJ", etc...

    Parameters
    ----------
    dados_mapeamento : pd.DataFrame
        base de dados desejada para a união
    coluna_estados : str
        coluna com a silga dos estados

    Returns
    -------
    pd.DataFrame
        dataframe com os dados do geobr uniados a base de dados desejada

    Raises
    ------
    TypeError
        Tipo incorreto do dataframe ou do nome da coluna
    ValueError
        Coluna não está na base de dados
    
    Test
    ----------
    >>> dados = pd.DataFrame({"PINCIPIO_ATIVO": ["CLOROQUINA", "DIFOSFATO DE CLOROQUINA", "HIDROXICLOROQUINA", "CLOROQUINA"], "UF": ["SP", "RJ", "CE", "MS"]})
    >>> type(mapeia_dados_estaduais(dados, "UF"))
    <class 'geopandas.geodataframe.GeoDataFrame'>
    
    >>> mapeia_dados_estaduais(66, "UF")
    Dataframe ou coluna de estados inválida, tente inserir outro dataframe ou a coluna como string.
    
    >>> mapeia_dados_estaduais(dados, 13)
    Dataframe ou coluna de estados inválida, tente inserir outro dataframe ou a coluna como string.

    >>> mapeia_dados_estaduais(dados, "COLUNA_INVÁLIDA")
    Coluna não encontrada no Dataframe, tente inserir uma coluna válida do dataframe.

    """
    try:
        # Valida a base de dados e o tipo da coluna
        if type(dados_mapeamento) != pd.DataFrame or type(coluna_estados) != str:
            raise TypeError
        # Valida a coluna na base de dados
        elif coluna_estados not in dados_mapeamento.columns:
            raise ValueError
    
    except TypeError:
        print("Dataframe ou coluna de estados inválida, tente inserir outro dataframe ou a coluna como string.")
    except ValueError:
        print("Coluna não encontrada no Dataframe, tente inserir uma coluna válida do dataframe.")

    else:
        # Realiza o merge entre o dataframe com os dados estaduais e o dataframe selecionado pela coluna de estados
        try:
            dados_estaduais = geobr.read_state()
            dados_estaduais.rename(columns={"abbrev_state": coluna_estados}, inplace=True)

            dados_resultantes = pd.merge(dados_estaduais, dados_mapeamento, on=coluna_estados, how="outer")

            return dados_resultantes
    
        except Exception as err:
            print("Erro encontrado:", err)


def gera_visualizacao_cloroquina(dados:pd.DataFrame, coluna_principio_ativo:str ="PRINCIPIO_ATIVO",
                                 coluna_estados="UF_VENDA", cmap="plasma", vmax=500, show_figure=False) -> plt.Axes:
    principios_ativos_cloroquina = [
        "CLOROQUINA",
        "DIFOSFATO DE CLOROQUINA",
        "HIDROXICLOROQUINA",
        "SULFATO DE HIDROXICLOROQUINA",
        "DICLORIDRATO DE CLOROQUINA",
        "SULFATO DE CLOROQUINA",
    ]
    fig, ax = plt.subplots(figsize=(10, 10))

    dados_filtrados = utils.filtra_dados_por_valores_procurados(dados, coluna_principio_ativo, principios_ativos_cloroquina)
    soma_vendas = soma_vendas_por_atributo(dados_filtrados, coluna_estados)
    dados_estaduais = mapeia_dados_estaduais(soma_vendas, coluna_estados)

    dados_estaduais["vendas"] = dados_estaduais["vendas"].fillna(0)
    
    dados_estaduais.plot(column="vendas", cmap=cmap, vmax=vmax, vmin=0, ax=ax, legend=True, edgecolor='k')

    fig.set_size_inches(8, 5.5)
    ax.axis('off')

    if show_figure == True:
        plt.show()

    return ax


def visualizacao_sillas(data_inicial:str, data_final:str, pasta_imagens:str, save_fig:bool =True) -> plt.Axes:
    datas = get_dates_between_dates(data_inicial, data_final)
    meses = {
        "01": 'Janeiro',
        "02": 'Fevereiro',
        "03": 'Março',
        "04": 'Abril',
        "05": 'Maio',
        "06": 'Junho',
        "07": 'Julho',
        "08": 'Agosto',
        "09": 'Setembro',
        "10": 'Outubro',
        "11": 'Novembro',
        "12": 'Dezembro'
    }

    for cada_data in datas:
        ano, mes = cada_data[:4], cada_data[-2:]

        dados = utils.concat_data_by_dates(cada_data, cada_data)

        ax = gera_visualizacao_cloroquina(dados=dados)
        ax.set_title(label=f"Venda de Cloroquina (e derivados) em\n{meses[mes]} de {ano}", loc="right")

        if save_fig == True:
            plt.savefig(f"{pasta_imagens}/frame_{cada_data[:4]}_{int(cada_data[-2:])}.png", dpi=500)

    return ax


if __name__ == "__main__":
    # dados = utils.concat_data_by_dates("2021/01", "2021/01")

    # visualizacao_sillas("2020/01", "2020/03", "..")

    # print(data["UF_VENDA"].value_counts())
    doctest.testmod(verbose=True)
