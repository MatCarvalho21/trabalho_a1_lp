import geobr
import pandas as pd
import matplotlib.pyplot as plt
import utils


def filtra_dados_por_valores_procurados(dados: pd.DataFrame, coluna_do_valor: str, valores_procurados: list) -> pd.DataFrame:
    dados = dados[dados[coluna_do_valor] in valores_procurados]

    return dados

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


def visualizacao_sillas():
    pass


if __name__ == "__main__":
    # dados = utils.concat_data_by_dates("2014/01", "2014/01")

    # dados = filtra_dados_por_valores_procurados(dados, "CID10", "A00")

    # dados = soma_vendas_por_atributo(dados, "UF_VENDA")

    # dados = mapeia_dados_estaduais(dados, "UF_VENDA")

    # print(dados)

    # print(data["UF_VENDA"].value_counts())