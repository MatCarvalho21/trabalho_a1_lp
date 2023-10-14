from get_data import get_dates_between_dates
import pandas as pd
import imageio


def concat_data_by_dates(start_date: str, end_date: str, path="dados", file_names="Manipulados", filtered_columns=None) -> pd.DataFrame:
    dates = get_dates_between_dates(start_date, end_date)
    first_date = dates[0]

    dataset = pd.read_csv(f"{path}/{file_names}_{first_date[:4]}_{first_date[-2:]}.csv",
                          delimiter=";", low_memory=False)
    
    if filtered_columns != None:
        dataset = dataset[filtered_columns]
    
    for index in range(1, len(dates)):
        date_year, date_month = dates[index][:4], dates[index][-2:]

        new_dataset = pd.read_csv(f"{path}/{file_names}_{date_year[:4]}_{date_month[-2:]}.csv",
                          delimiter=";", low_memory=False)
    
        if filtered_columns != None:
            new_dataset = new_dataset[filtered_columns]
        
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


