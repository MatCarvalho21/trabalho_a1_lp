"""Este módulo contém funções úteis para a manipulação da base de dados utilizando-se de datas, 
utilizada na visualização de alguns membros, além da filtragem dos dados.
"""

from get_data import get_dates_between_dates
import pandas as pd
import doctest


def concat_data_by_dates(start_date: str, end_date: str, path="dados", file_names="Manipulados", filtered_columns=None) -> pd.DataFrame:
    """
    Concatena todos os dados de CSVs de dados entre as datas dadas e retorna um dataframe Pandas
    O formato do nome dos arquivos devem ser 'nomedabase_ano_mes.csv'

    Parameters
    ----------
    start_date
        type: str
        description: inicio da range de datas 
        example: "2014-01"

    end_date
        type: str
        description: final da range de datas
        example: "2021-11"

    path
        type: str
        description: caminho da pasta com os arquivos
        example: "dados/"

    file_names
        type: str
        description: nome padrão de salvamento dos arquivos
        example: "file_names_ANO_mês.csv"
        
    filtered_columns
        type: list, optional
        description: colunas a serem filtradas se necessário da base de dados, caso não sejam válidas então todo o datafram é retornado
        example: "["coluna_1"]"

    Return
    ----------
    dataset
        type: pandas.Dataframe
        description: dataframe com todos os dados concatenados, caso as colunas de filtro sejam válidas, retorna o dataset com apenas elas como colunas.
    
    Test
    ----------
    >>> type(concat_data_by_dates("2014/01", "2014/01"))
    <class 'pandas.core.frame.DataFrame'>

    >>> len(concat_data_by_dates("2021/01", "2021/02", filtered_columns=["ANO_VENDA"]).columns)
    1

    >>> type(concat_data_by_dates("2021/01", "2021/01", filtered_columns=3))
    As colunas filtradas devem ser uma lista de strings das colunas do dataframe, tente inserir novamente.
    <class 'pandas.core.frame.DataFrame'>
    
    >>> type(concat_data_by_dates("2021/01", "2021/01", filtered_columns=["cachorro_mal"]))
    Uma ou mais colunas do filtro não estão nas colunas do dataframe, tente verificar as colunas do filtro.
    <class 'pandas.core.frame.DataFrame'>

    """
    try:
        # Valida as datas da concatenação.
        dates = get_dates_between_dates(start_date, end_date)
        if dates == []:
            raise ValueError
    except ValueError:
        pass

    else:
        first_date = dates[0]

        dataset = pd.read_csv(f"{path}/{file_names}_{first_date[:4]}_{first_date[-2:]}.csv",
                            delimiter=";", low_memory=False)
        # Verifica se o filtro é valido.
        if filtered_columns != None:
            try:
                if type(filtered_columns) != list:
                    raise TypeError
                for each_column in filtered_columns:
                    if each_column not in dataset.columns:
                        raise NameError

            except TypeError:
                print("As colunas filtradas devem ser uma lista de strings das colunas do dataframe, tente inserir novamente.")
            except NameError:
                print("Uma ou mais colunas do filtro não estão nas colunas do dataframe, tente verificar as colunas do filtro.")
            else:
                dataset = dataset[filtered_columns]

        if len(dates) > 1:
            for index in range(1, len(dates)):
                date_year, date_month = dates[index][:4], dates[index][-2:]
                try:
                    new_dataset = pd.read_csv(f"{path}/{file_names}_{date_year[:4]}_{date_month[-2:]}.csv",
                                    delimiter=";", low_memory=False)
                except Exception as err:
                    print(f"Não foi possível converter '{path}/{file_names}_{date_year[:4]}_{date_month[-2:]}.csv' em dataframe")
                    print(err)
                    continue
        
            new_dataset = new_dataset[dataset.columns]
            
            dataset = pd.concat([dataset, new_dataset])

        return dataset


def filtra_dados_por_valores_procurados(dados: pd.DataFrame, coluna_do_valor: str, valores_procurados: list or str) -> pd.DataFrame:
    """
    Modifica e retorna o dataframe com apenas as linhas que possuem o valor procurado na coluna especificada.

    Parameters
    ----------
    dados
        type: pandas.Dataframe
        description: dataframe a ser modificado
    
    coluna_do_valor
        type: str
        description: nome da coluna em que o valor deve estar 

    valores_procurados
        type: list or str
        description: valores que vão ser procurados na coluna e mantidos
        example: ["CLOROQUINA", "DISFOSFATO DE CLOROQUINA"]
    
    Return
    ----------
    dados
        type: pandas.Dataframe
        description: dataframe com apenas as linhas que contém o valor desejado

    Test
    ----------
    >>> dados = pd.DataFrame({"PINCIPIO_ATIVO": ["CLOROQUINA", "DIFOSFATO DE CLOROQUINA", "HIDROXICLOROQUINA", "IBUPROFENO"], "Qnt": [10, 5, 8, 15]})
    >>> filtra_dados_por_valores_procurados(dados, "PINCIPIO_ATIVO", "CLOROQUINA")["Qnt"][0]
    10

    >>> filtra_dados_por_valores_procurados(dados, "PINCIPIO_ATIVO", ["CLOROQUINA", "HIDROXICLOROQUINA"])["Qnt"]
    0    10
    2     8
    Name: Qnt, dtype: int64

    >>> filtra_dados_por_valores_procurados(42, "PINCIPIO_ATIVO", "CLOROQUINA")
    DataFrame inválido, tente inserir outro DataFrame.

    >>> filtra_dados_por_valores_procurados(dados, 66, "CLOROQUINA")
    Tente inserir um nome de coluna válido como string.

    >>> filtra_dados_por_valores_procurados(dados, "COLUNA_INVÁLIDA", "CLOROQUINA")
    Coluna selecionada inválida, tente inserir o nome de uma coluna do DataFrame.

    """
    # Chega se o data frame é válido.
    try:
        if type(dados) != pd.DataFrame:
            raise TypeError

    except TypeError:
        print("DataFrame inválido, tente inserir outro DataFrame.")

    else:
        # Checa se a coluna é válida.
        try:
            if type(coluna_do_valor) != str:
                raise TypeError
            elif coluna_do_valor not in dados.columns:
                raise ValueError
    
        except TypeError:
            print("Tente inserir um nome de coluna válido como string.")
        except ValueError:
            print("Coluna selecionada inválida, tente inserir o nome de uma coluna do DataFrame.")
    
        else:
            if type(valores_procurados) == list:
                dados = dados[dados[coluna_do_valor].isin(valores_procurados)]
            else:
                dados = dados[dados[coluna_do_valor] == valores_procurados]

            return dados


def set_anabolizantes(dataframe_bruto:pd.DataFrame) -> pd.DataFrame:
    """
    A função tem como objetivo receber um dataframe bruto e realizar a filtragem dos dados
    retornando apenas os registros referentes a medicamentos anabolizantes e esteróides. 

    Parameters
    ----------
    dataframe_bruto
        type: pd.DataFrame
        description: dataframe completo e referente a todos os medicamentos
    
    Return
    ----------
    dataframe_final
        type: pd.DataFrame
        description: dataframe filtrado apenas com os medicamentos anabolizantes

    Test
    ----------
    >>> type(set_anabolizantes(dataframe_geral))
    <class 'pandas.core.frame.DataFrame'>

    >>> dataframe_vazio = pd.DataFrame()
    >>> set_anabolizantes(dataframe_vazio)
    Esse dataframe está no formato incorreto, ele não possui a coluna 'PRINCIPIO_ATIVO'.

    >>> set_anabolizantes("Matheus")
    Algo deu errado. Verifique a documentação da função e tente novamente.
    """
    lista_de_anabolizantes = ["TESTOSTERONA",
                        "ESTANOZOLOL",
                        "NANDROLONA"]

    try: 
        #filtragem do dataframe
        df_testosterona = dataframe_bruto[dataframe_bruto["PRINCIPIO_ATIVO"] == lista_de_anabolizantes[0]].reset_index(drop=True)
        df_estanozolol = dataframe_bruto[dataframe_bruto["PRINCIPIO_ATIVO"] == lista_de_anabolizantes[1]].reset_index(drop=True)
        df_nandrolona = dataframe_bruto[dataframe_bruto["PRINCIPIO_ATIVO"] == lista_de_anabolizantes[2]].reset_index(drop=True)

        #concatenação do dataframe
        dataframe_final = pd.concat((df_testosterona, df_estanozolol, df_nandrolona)).reset_index(drop=True)

    except KeyError:
        print("Esse dataframe está no formato incorreto, ele não possui a coluna 'PRINCIPIO_ATIVO'.")
        dataframe_final = None
    except:
        print("Algo deu errado. Verifique a documentação da função e tente novamente.")
        dataframe_final = None
    
    return dataframe_final


if __name__ == "__main__":

    #dataframes para testes
    # df_01 = pd.read_csv("dados\Manipulados_2014_01.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    # df_02 = pd.read_csv("dados\Manipulados_2014_02.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    # df_03 = pd.read_csv("dados\Manipulados_2014_03.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    # dataframe_geral = pd.concat((df_01, df_02, df_03))
    dataframe_geral = concat_data_by_dates("2014/01", "2014/03", filtered_columns=["PRINCIPIO_ATIVO"])

    # print(concat_data_by_dates("2021/01", "2021/02", filtered_columns=["ANO_VENDA"]))

    doctest.testmod(verbose=True)