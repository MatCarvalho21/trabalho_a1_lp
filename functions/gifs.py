import pandas as pd
import imageio
import doctest

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

def gerador_de_gif(lista_de_frames:list, path_folder_for_save:str, output_name:str, fps:int) -> str:
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
    >>> gerador_de_gif(list(), "functions", "nome_genérico", fps=5)
    A lista fornecida deveria conter várias imagens para formar o gif. Verifique o parâmetro fornecido.
    """

    try: 
        imageio.mimsave(f"{path_folder_for_save}\{output_name}.gif", lista_de_frames, fps=fps)

    except PermissionError:
        print("O caminho fornecido é inválido. Tente novamente.")
        return None
    except ValueError:
        print("A lista fornecida deveria conter várias imagens para formar o gif. Verifique o parâmetro fornecido.")
        return None
    except:
        print("Algo deu errado. Verifique a documentação da função e tente novamente.")
        return None
    
    return "Deu tudo certo!"

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
    doctest.testmod()