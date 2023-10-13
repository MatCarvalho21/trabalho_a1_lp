import pandas as pd
import utils

def filtra_e_contatena(coluna_do_valor: str, valores_procurados: list or str):
    dataframe = utils.concat_data_by_dates(f"2014/01", f"2014/12")
    dataframe = utils.filtra_dados_por_valores_procurados(dataframe, coluna_do_valor, valores_procurados)
    for year in range(2014, 2021+1):
        novo_dataframe = utils.concat_data_by_dates(f"{year}/01", f"{year}/12")
        novo_dataframe = utils.filtra_dados_por_valores_procurados(novo_dataframe, coluna_do_valor, valores_procurados)
        dataframe = pd.concat((dataframe, novo_dataframe))
    
    return dataframe

if __name__ == "__main__":
    print(filtra_e_contatena("PRINCIPIO_ATIVO", "CLORIDRATO DE METILFENIDATO").head())
