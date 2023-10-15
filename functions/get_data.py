"""Módulo que coleta os dados de Venda de Medicamentos Controlados e Antimicrobianos (Medicamentos Manipulados)
do site "dados.gov.br", dados disponíveis de Janeiro de 2014 até Novembro de 2021.
Para a plena execução deste módulo, é necessário ter certeza de que o domínio
https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados
se encontra em pleno funcionamente e não está fora do ar, além disso, não houve alteração na forma como os dados são armazenados.
"""
import sys, os
esse_caminho = os.path.dirname(os.path.abspath(__file__))
sys.path.append(esse_caminho)

import pandas as pd
import os
import doctest


def validacao_datas(data_inicial:str, data_final:str) -> True:
    """Recebe duas datas e as valida para o formato desejado.

    Duas strings de datas, sendo que os primeiros 4 dígitos devem ser do ano e os últimos 2 do mês,
    a primeira data é a data inicial e a segunda a data final, a data final deve ser maior ou igual a data inicial,
    as duas datas devem estar entre Janeiro de 2014 (2014/01) e Novembro de 2021 (2021/11).

    Parameters
    ----------
    data_inicial : str
        A primeira data a ser validada.
    data_final : str
        A segunda data a ser validada, esta data deve ser posterior a primeira.

    Returns
    -------
    True
        Caso nenhum erro seja encontrado, ou seja, as datas sejam válidas

    Raises
    ------
    TypeError
        Tipo icorreto de datas.
    NameError
        Formato icorreto de datas.
    ValueError
        Problemas com os valores das datas, não estão entre Janeiro de 2014 e Novembro de 2021.
    IndexError
        A segunda data (data final) é menor do que a primeira data (data inicial).
    
    Test
    ----------
    >>> validacao_datas("2014/01", "2014/01")
    True

    >>> validacao_datas("2014/01", "2021/06")
    True

    >>> validacao_datas(2014/1, "2014/01")
    Tipo das datas inserido está incorreto, tente inserir a data como uma string, ex: '2015/05'
    
    >>> validacao_datas("2021", "2021/01")
    Formato das datas inserido está incorreto, revise novamente e tente inserir como ANO/mês, ex: '2015/05'.

    >>> validacao_datas("incorreto", "2021/01")
    Problemas com a primeira data inserida: inco/to
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.
    
    >>> validacao_datas("2014/01", "2022/01")
    Problemas com a segunda data inserida: 2022/01
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.
    """
    anos_validos = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    meses_validos = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    try:
        # Checa se o tipo da data é válido.
        if type(data_inicial) != str or type(data_final) != str:
            raise TypeError
        if len(data_inicial) < 6 or len(data_final) < 6:
            raise NameError
        
        ano_incial, mes_inicial = data_inicial[:4], data_inicial[-2:]
        ano_final, mes_final = data_final[:4], data_final[-2:]
    
        # Checa se o formato da data é válido.
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
        # Checa se a data final é maior ou igual a inicial
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
    else:
        return True


def get_dates_between_dates(data_inicial:str, data_final:str) -> list:
    """Recebe duas datas e retorna uma lista com todas as datas entre essas duas datas.
    
    A segunda data deve ser posterior a primeira, e do formato "AAAA/mm", além disso, as datas devem
    estar entre Janeiro de 2014 e Novembro de 2021. Possui as mesmas exceções da função "validacao_datas".

    Parameters
    ----------
    data_inicial : str
        A primeira data a ser validada.
    data_final : str
        A segunda data a ser validada, esta data deve ser posterior a primeira.

    Returns
    -------
    lista_datas : list
        Uma lista com todas as datas entre a data inicial e a data final, as datas
        estão no formato de string "AAAAmm". Caso as datas não sejam válidas, retorna uma lista vazia.

    Test
    ----------
    >>> get_dates_between_dates("2014/01", "2014/01")
    ['201401']

    >>> get_dates_between_dates("2021/08", "2021/11")
    ['202108', '202109', '202110', '202111']

    >>> get_dates_between_dates("2014/01", "2030/06")
    Problemas com a segunda data inserida: 2030/06
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.
    []

    >>> get_dates_between_dates("2015/01", "2014/06")
    A segunda data deve ser maior ou igual a primeira, ex: ('2014/01', '2014/01') ou ('2014/01', '2016/02')
    []
    """
    lista_datas = []
    try:
        # Valida a data antes de proseguir com o código
        if validacao_datas(data_inicial, data_final) != True:
            raise Exception
    except:
        return lista_datas
    else:
        ano_inicial = int(data_inicial[:4])
        mes_inicial = int(data_inicial[-2:])
        ano_final = int(data_final[:4])
        mes_final = int(data_final[-2:])

        # loop para adicionar todas as datas no formato "AAAAmm" à lista.
        while ano_inicial <= ano_final:
            data_atual = f"{ano_inicial}{mes_inicial:02}"
            lista_datas.append(data_atual)
            
            if ano_inicial == ano_final and mes_inicial == mes_final:
                break
            elif mes_inicial == 12:
                ano_inicial += 1
                mes_inicial = 1
            else:
                mes_inicial += 1

        return lista_datas


def download_csv_by_dates(data_inicial:str, data_final:str = None, output_file:str = None) -> pd.DataFrame:
    """Função para baixar os dados da base de dados pelas datas selecionadas.

    Como todos os dados da base de dados em csv podem ser baixados a partir dos links: 
    "https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{data}.csv", onde a data
    se encontra no formato "AAAAmm" (ex: "201401", ou seja, Janeiro de 2014), essa função baixa esses
    dados através do pandas e os retorna como um dataframe, podendo escolher entre apenas uma data ou todos os
    dados entre duas datas, é possível também transformá-los em arquivos de saída definindo o
    output_file, com o caminho e nome do arquivo desejado, o arquivo deve conter ".csv" no final,
    a base de dados contém registros desde Janeiro de 2014 até Novembro de 2021, por isso,
    é feita uma validação de datas através da função validacao_datas, e nem sempre o servidor possui resposta.

    Parameters
    ----------
    data_inicial : str
        A data do primeiro registro buscado.
    data_final : str, optional
        A data do último registro buscado, by default None
    output_file : str, optional
        O caminho e nome do arquivo de saída, by default None

    Returns
    -------
    pd.DataFrame
        O dataframe dos registros da base de dados da data ou datas inseridas.

    Raises
    ------
    ValueError
        O arquivo de saída não é uma string ou não acaba em .csv
        
    Test
    ----------
    >>> download_csv_by_dates(2021)
    Tipo das datas inserido está incorreto, tente inserir a data como uma string, ex: '2015/05'

    >>> download_csv_by_dates("2021/01", "2028/12")
    Problemas com a segunda data inserida: 2028/12
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.

    >>> download_csv_by_dates("2021/01", output_file=3)
    O arquivo de saída deve ser uma string e terminar em .csv, ex: 'caminho/meu_arquivo.csv'

    >>> download_csv_by_dates("2021/01", output_file="caminho/test.txt")
    O arquivo de saída deve ser uma string e terminar em .csv, ex: 'caminho/meu_arquivo.csv'

    """
    try:
        # Valida a data antes de prosseguir com o código.
        if data_final != None:
            if validacao_datas(data_inicial, data_final) != True:
                raise BaseException
        else:
            if validacao_datas(data_inicial, data_inicial) != True:
                raise BaseException
        # Valida o arquivo de saída.
        if output_file != None:
            if type(output_file) != str:
                raise ValueError
            elif output_file[-4:] != ".csv":
                raise ValueError

        dataset = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{data_inicial}.csv", delimiter=";", encoding="unicode_escape", low_memory=False)

        if data_final != None:
            dates = get_dates_between_dates(data_inicial, data_final)
            # Concatena os arquivos de diferentes datas se necessário.
            for index in range(1, len(dates)):
                new_year_data = pd.read_csv(f"https://dados.anvisa.gov.br/dados/SNGPC/Manipulados/EDA_Manipulados_{dates[index]}.csv", delimiter=";", low_memory=False)
                dataset = pd.concat([dataset, new_year_data])

        dataset.to_csv(output_file, sep=";", index=False)
        
        return dataset

    except ValueError:
        print("O arquivo de saída deve ser uma string e terminar em .csv, ex: 'caminho/meu_arquivo.csv'")
    except Exception as err:
        print("Houve um erro:", err, end=". ")
    except BaseException:
        return


def download_data_sep_by_months(data_incial:str, data_final:str, caminho:str) -> None:
    """Baixa arquivos da base de dados separadamente por meses

    Devido as limitações do github para arquivos de tamanhos grandes, essa função baixa os arquivos
    separadamente por mês e ano, os salvando da forma "Manipulados_AAAA_mm.csv", ex: Manipulados_2014_01.csv.
    Os dados de medicamentos manipulados de Janeiro de 2014. as validações de datas são feitas seguindo a função
    "validacao_datas". A função está também limitada ao pleno funcionamento do site
    https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados


    Parameters
    ----------
    data_incial : str
        A data do primeiro registro a ser baixado.
    data_final : str
        A data do último registro a ser baixado.
    caminho : str
        O caminho em que os arquivos serão baixados.

    Test
    ----------
    >>> download_data_sep_by_months("2014/01", "201401", 3)
    Caminho deve ser uma string, tente iserir outro caminho.

    >>> download_data_sep_by_months("2013/01", "2015/01", 3)
    Problemas com a primeira data inserida: 2013/01
    Formato da data está incorreto ou ela não está entre Janeiro de 2014 e Novembro de 2021, tente inserir como ANO/mês, ex: '2015/05'.

    """
    # Pega as datas selecionadas e faz a validação.
    datas_selecionadas = get_dates_between_dates(data_incial, data_final)
    
    # Confirma se o caminho é do tipo válido e se as datas foram válidas.
    try:
        if datas_selecionadas == []:
            raise ValueError
        if type(caminho) != str:
            raise TypeError
    except TypeError:
        print("Caminho deve ser uma string, tente iserir outro caminho.")
    except ValueError:
        return
    else:
        for cada_data in datas_selecionadas:
            nome_arquivo = f"Manipulados_{cada_data[:4]}_{cada_data[-2:]}.csv"
            try:
                # Tenta baixar os arquivos e se eles não forem baixados levanda a exceção.
                dados = download_csv_by_dates(cada_data, output_file=os.path.join(caminho, nome_arquivo))
                if type(dados) == type(None):
                    raise Exception
                print(nome_arquivo, "Adicionado com Sucesso!")

            except Exception as err:
                print(f"Falha ao baixar {nome_arquivo}. {err}")


if __name__ == "__main__":
    # Baixando os dados para que eles fiquem salvos para futuras manipulações
    """
    esse_caminho = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(esse_caminho, "..", "dados")

    print(download_data_sep_by_months("2014/01", "2021/11", caminho_completo))
    """
    
    doctest.testmod(verbose=True)
    
