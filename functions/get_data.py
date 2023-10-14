"""Módulo que coleta os dados de Venda de Medicamentos Controlados e Antimicrobianos (Medicamentos Manipulados)
do site "dados.gov.br", dados disponíveis de Janeiro de 2014 até Novembro de 2021.
Para a plena execução deste módulo, é necessário ter certeza de que o domínio
https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados
se encontra em pleno funcionamente e não está fora do ar, além disso, não houve alteração na forma como os dados são armazenados.
"""

import pandas as pd
import os
from urllib.request import urlretrieve

def validate_dates():
    pass

def get_dates_between_dates(data_inicial: str, data_final: str) -> list:
    lista_datas = []
    ano_inicial = int(data_inicial[:4])
    mes_inicial = int(data_inicial[-2:])
    ano_final = int(data_final[:4])
    mes_final = int(data_final[-2:])

    while ano_inicial <= ano_final:
        date = f"{ano_inicial}{mes_inicial:02}"
        lista_datas.append(date)
        
        if ano_inicial == ano_final and mes_inicial == mes_final:
            break
        elif mes_inicial == 12:
            ano_inicial += 1
            mes_inicial = 1
        else:
            mes_inicial += 1

    return lista_datas


def data_to_csv_by_dates(data_inicial: str, data_final=None, output_file=None) -> pd.DataFrame:
    dataset = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{data_inicial}.csv", delimiter=";", encoding="unicode_escape", low_memory=False)

    if data_final != None:
        dates = get_dates_between_dates(data_inicial, data_final)

        for index in range(1, len(dates)):
            new_year_data = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{dates[index]}.csv", delimiter=";", low_memory=False)
            dataset = pd.concat([dataset, new_year_data])

    dataset.to_csv(output_file, sep=";", index=False)

    return dataset


def download_data_sep_by_months(data_incial: str, data_final: str, caminho: str) -> None:
    datas_selecionadas = get_dates_between_dates(data_incial, data_final)

    for cada_data in datas_selecionadas:
        nome_arquivo = f"Manipulados_{cada_data[:4]}_{cada_data[-2:]}.csv"
        try:
            data_to_csv_by_dates(cada_data, output_file=os.path.join(caminho, nome_arquivo))
            print(nome_arquivo, "Adicionado com Sucesso!")
        except Exception as err:
            print(f"Falha ao baixar {nome_arquivo}: {err}")


if __name__ == "__main__":
    # Baixando os dados para que eles fiquem salvos para futuras manipulações
    esse_caminho = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(esse_caminho, "..", "dados")

    download_data_sep_by_months("2014/01", "2021/11", caminho_completo)

