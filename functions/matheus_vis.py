from dados_anabolizantes import set_anabolizantes
import pandas as pd  
import matplotlib.pyplot as plt 

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
dataframe_geral["NUMERO_DE_VENDAS"] = 1

x_meses = range(1, 13)

figure, axis = plt.subplots(nrows=2, 
                                    ncols=2, 
                                    sharex=True,
                                    figsize=(15, 12))

#TESTOSTERONA
df_testosterona = (dataframe_geral[dataframe_geral["PRINCIPIO_ATIVO"] == "TESTOSTERONA"]).reset_index(drop=True).groupby("MES_VENDA").sum()
y_testosterona = list(df_testosterona["NUMERO_DE_VENDAS"])

axis[0, 0].set_title('Testosterona')
axis[0, 0].errorbar(x_meses, y_testosterona)


#ESTANOZOLOL
df_estanozolol = (dataframe_geral[dataframe_geral["PRINCIPIO_ATIVO"] == "ESTANOZOLOL"]).reset_index(drop=True).groupby("MES_VENDA").sum()
y_estanozolol = list(df_estanozolol["NUMERO_DE_VENDAS"])

axis[0, 1].set_title('Estanozolol')
axis[0, 1].errorbar(x_meses, y_estanozolol)

#METANDIENONA

df_metandienona = (dataframe_geral[dataframe_geral["PRINCIPIO_ATIVO"] == "METANDIENONA"]).reset_index(drop=True).groupby("MES_VENDA").sum()
y_metandienona = list(df_metandienona["NUMERO_DE_VENDAS"])

if len(y_metandienona) < 12:
    y_metandienona = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


axis[1, 0].set_title('Metandienona')
axis[1, 0].errorbar(x_meses, y_metandienona)

#NANDROLONA
df_nandrolona = (dataframe_geral[dataframe_geral["PRINCIPIO_ATIVO"] == "NANDROLONA"]).reset_index(drop=True).groupby("MES_VENDA").sum()
y_nandrolona = list(df_nandrolona["NUMERO_DE_VENDAS"])

axis[1, 1].set_title('Nandrolona')
axis[1, 1].errorbar(x_meses, y_nandrolona)

plt.show()
