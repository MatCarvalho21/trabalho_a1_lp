"""Módulo de visualização do integrande Sillas Rocha, possui 4 funções
que servem para explorar a base de dados e fazer plotagens relacionando
as vendas de remédios Manipulados de cloroquina por estado, nas datas
selecionadas, e por fim, salvar essas plotagens em alguma imagem.
"""

import sys, os
esse_caminho = os.path.dirname(os.path.abspath(__file__))
sys.path.append(esse_caminho)

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
                                 coluna_estados="UF_VENDA", cmap="plasma", vmax=400, show_figure=False) -> plt.Axes:
    """Função que usa a biblioteca geobr e a base de dados de medicamentos manipulados para criar uma plotagem.

    A função recebe os dados pertinentes da análise e cria uma plotagem baseada no número de vendas
    da Cloroquina e derivados nos estados brasileiros como um heatmap. Em virtude de reduzir
    outliers, como São Paulo, do heatmap, o vmax, que limita o valor máximo da coloração foi reduzido.

    Parameters
    ----------
    dados : pd.DataFrame
        Dataframe com os dados a serem análisados
    coluna_principio_ativo : str, optional
        Coluna do data frame que vai ser contabilizada nos estados, by default "PRINCIPIO_ATIVO"
    coluna_estados : str, optional
        Coluna dos estados como siglas, ex: "SP", by default "UF_VENDA"
    cmap : str, optional
        Color map da visualização, deve ser um color map válido do matplotlib, by default "plasma"
    vmax : int, optional
        Valor máximo do heatmap, by default 400
    show_figure : bool, optional
        Opção para exibir a figura gerada automaticamente, by default False

    Returns
    -------
    plt.Axes
        A figura gerada pela plotagem.

    Raises
    ------
    TypeError
        Tipo do dataframe inválido.
    ValueError
        Colunas de estados e do princípio ativo fora da base de dados.
        
    Test
    ----------
    >>> gera_visualizacao_cloroquina(3)
    Dataframe inválido, tente inserir Dataframe.

    >>> gera_visualizacao_cloroquina(pd.DataFrame())
    Coluna de estados e da contabilização de vendas devem ser colunas válidas do Dataframe. Tente inserir novas colunas.

    """
    principios_ativos_cloroquina = [
        "CLOROQUINA",
        "DIFOSFATO DE CLOROQUINA",
        "HIDROXICLOROQUINA",
        "SULFATO DE HIDROXICLOROQUINA",
        "DICLORIDRATO DE CLOROQUINA",
        "SULFATO DE CLOROQUINA",
    ]
    fig, ax = plt.subplots(figsize=(10, 10))
    # filtra para apenas os dados com cloroquina
    try:
        if type(dados) != pd.DataFrame:
            raise TypeError
        elif coluna_estados not in dados.columns or coluna_principio_ativo not in dados.columns:
            raise ValueError
    
    except TypeError:
        print("Dataframe inválido, tente inserir Dataframe.")
    except ValueError:
        print("Coluna de estados e da contabilização de vendas devem ser colunas válidas do Dataframe. Tente inserir novas colunas.")

    else:
        dados_filtrados = utils.filtra_dados_por_valores_procurados(dados, coluna_principio_ativo, principios_ativos_cloroquina)
        # contabiliza a soma das vendas destes remédios por estado
        soma_vendas = soma_vendas_por_atributo(dados_filtrados, coluna_estados)
        # une a soma das vendas aos dados estaduais da biblioteca geobr
        dados_estaduais = mapeia_dados_estaduais(soma_vendas, coluna_estados)

        # preenche como 0 os valores nulos para que eles continuam aparecendo no mapa
        dados_estaduais["vendas"] = dados_estaduais["vendas"].fillna(0)
        # cria uma plotagem do brasil com a quantidade de vendas em cada estado
        dados_estaduais.plot(column="vendas", cmap=cmap, vmax=vmax, vmin=0, ax=ax, legend=True, edgecolor='k')
        # ajeita as proporções da plotagem
        fig.set_size_inches(8, 5.5)
        ax.axis('off')

        if show_figure == True:
            plt.show()

        return ax


def visualizacao_sillas(data_inicial:str, data_final:str, pasta_imagens:str, save_fig:bool =True) -> plt.Axes:
    """Gera imagens a partir de duas datas, da base de dados e da função gera_visualizacao_cloroquina.

    A visualização final se baseia em mostrar o aumento da procura por cloroquina com o passar do tempo,
    por isso, esta função receberá duas datas, uma inicial e uma final, e as converterá em visualizações
    da cloroquina para cada data entre estas duas datas, de entrada, além disso é necessário informar o
    diretório em que as pastas ficarão salvas.

    Parameters
    ----------
    data_inicial : str
        Data inicial da amostragem de dados
    data_final : str
        Data final da amostragem de dados
    pasta_imagens : str
        Diretório onde as imagens serão salvas
    save_fig : bool, optional
        Define se as imagens serão salvas ou não, by default True

    Raises
    ------
    IndexError
        Valida as datas de entrada.
    
    Test
    ----------
    >>> visualizacao_sillas("2014/01", "2014/01", "DIRETÓRIO_INVÁLIDO")
    Não foi possível salvar frame_2014_1.png, erro: [Errno 2] No such file or directory: 'DIRETÓRIO_INVÁLIDO/frame_2014_1.png'

    >>> visualizacao_sillas("2013/01", "2015/02", "seu_caminho")
    Problemas com a primeira data inserida: 2013/01
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.
    
    """
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

    try:
        if datas == []:
            raise IndexError
    except IndexError:
        pass
    else:
        for cada_data in datas:
            ano, mes = cada_data[:4], cada_data[-2:]

            dados = utils.concat_data_by_dates(cada_data, cada_data)

            ax = gera_visualizacao_cloroquina(dados=dados)
            ax.set_title(label=f"Venda de Cloroquina (e derivados) em\n{meses[mes]} de {ano}", loc="right")

            if save_fig == True:
                nome_frame = f"frame_{cada_data[:4]}_{int(cada_data[-2:])}.png"
                try:
                    plt.savefig(f"{pasta_imagens}/{nome_frame}", dpi=500)
                except Exception as err:
                    print(f"Não foi possível salvar {nome_frame}, erro:", err)


if __name__ == "__main__":

    # print(visualizacao_sillas("2020/01", "2021/03", ".."))

    doctest.testmod(verbose=True)
