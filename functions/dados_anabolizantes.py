import pandas as pd   
import doctest

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

    >>> set_anabolizantes(dataframe_vazio)
    Esse dataframe está no formato incorreto, ele não possui a coluna 'PRINCIPIO_ATIVO'.

    >>> set_anabolizantes("Matheus")
    Algum erro inesperado aconteceu, verifique a base de dados.

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
        print("Algum erro inesperado aconteceu, verifique a base de dados.")
        dataframe_final = None
    
    return dataframe_final

if __name__ == "__main__":

    #dataframes para testes
    df_01 = pd.read_csv("dados\Manipulados_2014_01.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_02 = pd.read_csv("dados\Manipulados_2014_02.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_03 = pd.read_csv("dados\Manipulados_2014_03.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_04 = pd.read_csv("dados\Manipulados_2014_04.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_05 = pd.read_csv("dados\Manipulados_2014_05.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_06 = pd.read_csv("dados\Manipulados_2014_06.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_07 = pd.read_csv("dados\Manipulados_2014_07.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_08 = pd.read_csv("dados\Manipulados_2014_08.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_09 = pd.read_csv("dados\Manipulados_2014_09.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_10 = pd.read_csv("dados\Manipulados_2014_10.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_11 = pd.read_csv("dados\Manipulados_2014_11.csv", delimiter=";", encoding="unicode_escape", low_memory=False)
    df_12 = pd.read_csv("dados\Manipulados_2014_12.csv", delimiter=";", encoding="unicode_escape", low_memory=False)

    dataframe_geral = pd.concat((df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, df_09, df_10, df_11, df_12))

    dataframe_vazio = pd.DataFrame()

    doctest.testmod()
