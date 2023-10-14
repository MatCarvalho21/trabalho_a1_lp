"""Este módulo contém funções úteis para a manipulação da base de dados utilizando-se de datas
e a conversão de imagens em gifs, utilizada na visualização de alguns membros, além da filtragem
dos dados.
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


def seletor_de_frames(data_inicial:str, data_final:str, path_pasta_imagens:str) -> list:
    """
    A função recebe a data_inicial e a data_final, elas criam uma range de imagens, além disso 
    o path relativo da pasta que contém as imagens em questão. Ela, então, cria uma lista com 
    as imagens e a retorna para que possam ser concatenadas em um gif. 

    Parameters
    ----------
    data_inicial
        type: str
        description: inicio da range de datas 
        example: "2020"

    data_final
        type: str
        description: final da range de datas
        example: "2021"

    path_pasta_imagens
        type: str
        description: 
        example: "root\\folder_01\\final_folder"

    Return
    ----------
    lista_de_frames
        type: list
        description: lista com as imagens que irão compor o gif da visualização 


    Test
    ----------
    >>> seletor_de_frames("2014", "2016", "pasta_inexistente")
    Não foi possível encontrar nenhum frame. Certifique de que o caminho fornecido está correto.
    """

    lista_de_frames = list()

    try:
        # selecionando os frames
        for cada_ano in range(int(data_inicial), int(data_final) + 1):
            for cada_mes in range(1, 13):
                frame = imageio.v2.imread(f"{path_pasta_imagens}\\frame_{cada_ano}_{cada_mes}.png")
                lista_de_frames.append(frame)

    except FileNotFoundError:
        print("Não foi possível encontrar nenhum frame. Certifique de que o caminho fornecido está correto.")
        lista_de_frames = None
    except:
        print("Algo deu errado. Verifique a documentação da função e tente novamente.")
        lista_de_frames = None

    return lista_de_frames


def gerador_de_gif(lista_de_frames:list, path_folder_for_save:str, output_name:str) -> None:
    """
    A função tem como objetivo criar vários frames, separados por ano e por mês, 
    para que eles sejam usados em um gráfico animado. Ela vai gerar várias imagens
    que serão utilizadas para montar a visualização animada.

    Parameters
    ----------
    lista_de_frames
        type: list
        description: lista com frames que devem compor o gif
    
    path_folder_for_save
        type: str
        description: path da pasta para salvar o arquivo 
        example: "root\\folder_01\\final_folder"

    output_name
        type: str
        description: nome do arquivo que vai ser gerado e salvo
        example: "meu_gif"

    Test
    ----------
    >>> gerador_de_gif(list(), "functions", "nome_genérico")
    A lista fornecida deveria conter várias imagens para formar o gif. Verifique o parâmetro fornecido.
    """

    try: 
        imageio.mimsave(f"{path_folder_for_save}\{output_name}.gif", lista_de_frames, fps=4)

    except PermissionError:
        print("O caminho fornecido é inválido. Tente novamente.")
    except ValueError:
        print("A lista fornecida deveria conter várias imagens para formar o gif. Verifique o parâmetro fornecido.")
    except:
        print("Algo deu errado. Verifique a documentação da função e tente novamente.")


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


if __name__ == "__main__":

    # print(concat_data_by_dates("2021/01", "2021/02", filtered_columns=["ANO_VENDA"]))

    doctest.testmod(verbose=True)