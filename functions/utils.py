from get_data import get_dates_between_dates
import pandas as pd

def concat_data(start_date: str, end_date: str, path="dados", file_name="Manipulados"):
    dates = get_dates_between_dates(start_date, end_date)
    first_date = dates[0]

    dataset = pd.read_csv(f"{path}/{file_name}_{first_date[:4]}_{first_date[-2:]}.csv",
                          delimiter=";", low_memory=False)
    
    for index in range(1, len(dates)):
        date_year, date_month = dates[index][:4], dates[index][-2:]

        new_dataset = pd.read_csv(f"{path}/{file_name}_{date_year[:4]}_{date_month[-2:]}.csv",
                          delimiter=";", low_memory=False)
        
        dataset = pd.concat([dataset, new_dataset])

    return dataset

