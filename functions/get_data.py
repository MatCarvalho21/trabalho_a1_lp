"""Módulo que coleta os dados de Venda de Medicamentos Controlados e Antimicrobianos (Medicamentos Manipulados)
do site "dados.gov.br", dados disponíveis de Janeiro de 2014 até Novembro de 2021.
Para a plena execução deste módulo, é necessário ter certeza de que o domínio
https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados
se encontra em pleno funcionamente e não está fora do ar, além disso, não houve alteração na forma como os dados são armazenados.
"""

import pandas as pd
import os
from urllib.request import urlretrieve


def validacao_datas(data_inicial: str, data_final: str):
    anos_validos = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    meses_validos = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    try:
        if type(data_inicial) != str or type(data_final) != str:
            raise TypeError
        if len(data_inicial) < 6 or len(data_final) < 6:
            raise NameError
        
        ano_incial, mes_inicial = data_inicial[:4], data_inicial[-2:]
        ano_final, mes_final = data_final[:4], data_final[-2:]

        if ano_incial not in anos_validos or mes_inicial not in meses_validos:
            print("Problemas com a primeira data inserida:", f"{ano_incial}/{mes_inicial}")
            raise ValueError
        elif ano_final not in anos_validos or mes_final not in meses_validos:
            print("Problemas com a segunda data inserida:", f"{ano_final}/{mes_final}")
            raise ValueError
        elif mes_inicial == "12" and ano_incial == "2021":
            raise ValueError
        elif mes_final == "12" and ano_final == "2021":
            raise ValueError
        elif anos_validos.index(ano_final) < anos_validos.index(ano_incial):
            raise IndexError
        elif ano_final == ano_incial and meses_validos.index(mes_final) < meses_validos.index(mes_inicial):
            raise IndexError
        
    except TypeError:
        print("Tipo das datas inserido está incorreto, tente inserir a data como uma string, ex: '2015/05'")
    except NameError:
        print("Formato das datas inserido está incorreto, revise novamente e tente inserir como ANO/mês, ex: '2015/05'.")
    except ValueError:
        print("Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.")
    except IndexError:
        print("A segunda data deve ser maior ou igual a primeira, ex: ('2014/01', '2014/01') ou ('2014/01', '2016/02')")

    except Exception as err:
        print("Outro erro encontrado:", err)


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
    # esse_caminho = os.path.dirname(os.path.abspath(__file__))
    # caminho_completo = os.path.join(esse_caminho, "..", "dados")

    # download_data_sep_by_months("2014/01", "2021/11", caminho_completo)

    # validacao_datas("2015/05", "2015/04")
