"""Este módulo contém funções úteis para a manipulação da base de dados utilizando-se de datas, 
utilizada na visualização de alguns membros, além da filtragem dos dados.
"""

from get_data import get_dates_between_dates
import pandas as pd
import imageio
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


if __name__ == "__main__":

    # print(concat_data_by_dates("2021/01", "2021/02", filtered_columns=["ANO_VENDA"]))

    doctest.testmod(verbose=True)