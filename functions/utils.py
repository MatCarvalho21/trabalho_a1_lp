from get_data import get_dates_between_dates
import pandas as pd


def concat_data_by_dates(start_date: str, end_date: str, path="dados", file_names="Manipulados", filtered_columns=None) -> pd.DataFrame:
    dates = get_dates_between_dates(start_date, end_date)
    first_date = dates[0]

    dataset = pd.read_csv(f"{path}/{file_names}_{first_date[:4]}_{first_date[-2:]}.csv",
                          delimiter=";", low_memory=False)
    
    if filtered_columns != None:
        dataset = dataset[filtered_columns]
    
    for index in range(1, len(dates)):
        date_year, date_month = dates[index][:4], dates[index][-2:]
        try:
            new_dataset = pd.read_csv(f"{path}/{file_names}_{date_year[:4]}_{date_month[-2:]}.csv",
                            delimiter=";", low_memory=False)
        except Exception as err:
            print(f"Não foi possível converter '{path}/{file_names}_{date_year[:4]}_{date_month[-2:]}.csv' em dataframe")
            print(err)
            continue
    
        if filtered_columns != None:
            new_dataset = new_dataset[filtered_columns]
        
        dataset = pd.concat([dataset, new_dataset])

    return dataset


def filtra_dados_por_valores_procurados(dados: pd.DataFrame, coluna_do_valor: str, valores_procurados: list or str) -> pd.DataFrame:
    if type(valores_procurados) == list:
        dados = dados[dados[coluna_do_valor].isin(valores_procurados)]
    elif type(valores_procurados) == str:
        dados = dados[dados[coluna_do_valor] == valores_procurados]

    return dados

