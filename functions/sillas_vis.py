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


def visualizacao_sillas(data_inicial: str, data_final: str, pasta_imagens: str, save_fig=True) -> plt.Axes:
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
    pass
