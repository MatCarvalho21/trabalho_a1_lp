import geobr
import pandas as pd
import matplotlib.pyplot as plt
import utils
from get_data import get_dates_between_dates


def soma_vendas_por_atributo(dados: pd.DataFrame, atributo: str) -> pd.DataFrame:
    soma_vendas = pd.DataFrame()
    vendas_totais = dados.value_counts(atributo)

    soma_vendas[atributo] = vendas_totais.index
    soma_vendas["vendas"] = vendas_totais.values

    return soma_vendas


def mapeia_dados_estaduais(dados_mapeamento: pd.DataFrame, coluna_estados: str,) -> pd.DataFrame:
    dados_estaduais = geobr.read_state()
    dados_estaduais.rename(columns={"abbrev_state": coluna_estados}, inplace=True)

    dados_resultantes = pd.merge(dados_estaduais, dados_mapeamento, on=coluna_estados, how="outer")

    return dados_resultantes


def gera_visualizacao_cloroquina(dados: pd.DataFrame, coluna_principio_ativo="PRINCIPIO_ATIVO",
                                 coluna_estados="UF_VENDA", cmap="plasma", vmax=3052, show_figure=False) -> pd.DataFrame:
    principios_ativos_cloroquina = [
        "CLOROQUINA",
        "DIFOSFATO DE CLOROQUINA",
        "HIDROXICLOROQUINA",
        "SULFATO DE HIDROXICLOROQUINA",
        "DICLORIDRATO DE CLOROQUINA",
        "SULFATO DE CLOROQUINA",
    ]
    fig, ax = plt.subplots(figsize=(15, 15))

    dados_filtrados = utils.filtra_dados_por_valores_procurados(dados, coluna_principio_ativo, principios_ativos_cloroquina)
    soma_vendas = soma_vendas_por_atributo(dados_filtrados, coluna_estados)
    dados_estaduais = mapeia_dados_estaduais(soma_vendas, coluna_estados)
    
    dados_estaduais.plot(column="vendas", cmap=cmap, vmax=vmax, vmin=0, ax=ax, legend=True)

    if show_figure == True:
        plt.show()

    return dados_estaduais


def visualizacao_sillas():
    pass


if __name__ == "__main__":
    # dados = utils.concat_data_by_dates("2021/01", "2021/01")

    # print(gera_visualizacao_cloroquina(dados, show_figure=True))


    pass
