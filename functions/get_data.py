"""Módulo que coleta os dados de Venda de Medicamentos Controlados e Antimicrobianos (Medicamentos Manipulados)
do site "dados.gov.br", dados disponíveis de Janeiro de 2014 até Novembro de 2021.
Para a plena execução deste módulo, é necessário ter certeza de que o domínio
https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados
se encontra em pleno funcionamente e não está fora do ar, além disso, não houve alteração na forma como os dados são armazenados.
"""

import pandas as pd


def validate_dates():
    pass

def get_dates_between_dates(first_date: str, final_date: str):
    dates_list = []
    first_year = int(first_date[:4])
    first_month = int(first_date[-2:])
    final_year = int(final_date[:4])
    final_month = int(final_date[-2:])

    while first_year <= final_year:
        date = f"{first_year}{first_month:02}"
        dates_list.append(date)
        
        if first_year == final_year and first_month == final_month:
            break
        elif first_month == 12:
            first_year += 1
            first_month = 1
        else:
            first_month += 1

    return dates_list


def data_to_csv_by_dates(start_date: str, end_date=None, output_file=None):
    dataset = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{start_date}.csv", delimiter=";", encoding="unicode_escape", low_memory=False)

    if end_date != None:
        dates = get_dates_between_dates(start_date, end_date)

        for i in range(1, len(dates)):
            new_year_data = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{dates[i]}.csv", delimiter=";", low_memory=False)
            dataset = pd.concat([dataset, new_year_data])

    dataset.to_csv(output_file, sep=";", index=False)

    return dataset


if __name__ == "__main__":
    # Baixando os dados para que eles fiquem salvos para futuras manipulações
    """
    datas_disponiveis = get_dates_between_dates("2014/01", "2021,11")
    for cada_data in datas_disponiveis:
        nome_arquivo = f"Manipulados_{cada_data[:4]}_{cada_data[-2:]}.csv"
        data_to_csv_by_dates(cada_data, f"dados/{nome_arquivo}")
        print(nome_arquivo, "Adicionado com Sucesso!")
    """

