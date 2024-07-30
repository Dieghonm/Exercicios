#para rodar = python3 1-Python/Exercicios/EBAC/Mpython11/extracao.py

import pandas as pd


URL = 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/credito.csv'
df = pd.read_csv(URL, na_values=['na', '', None]) # esta linha mostra ao pandas quais os tipos de dados ele deve coiciderar dados faltantes

# print(df.head(n=5)) # mostra s 5 primeiras linhas
total, _ = df.shape # mostra o numero de linhas e colunas

adimplentes, _ = df[df['default'] == 0].shape #conta quantas linhas possui 0 na coluna 'default'
inadimplentes, _ = df[df['default'] == 1].shape #conta quantas linhas possui 1 na coluna 'default'

# print(f'clientes adimplentes sao {round(100 * adimplentes / total, 2)}%')
# print(f'clientes inadimplentes sao {round(100 * inadimplentes / total, 2)}%')

# print(f'{df.dtypes}') # mostra o tipo de dado em cada coluna
tipo_Object = df.select_dtypes("object") # mostra as colunas com o tipo especifico de dado
soma = tipo_Object.describe() # soma os dados para melhorar a visualização
vert = soma.transpose() # vira o dado para a vertical
# print(f'->{vert}') 

tipo_Number = df.drop('id', axis=1).select_dtypes('number').describe().transpose() # o drop retira uma coluna
# print(f'->{tipo_Number}') 

dados_faltantes = df.isna().any() #mostra quais colunas tem dados incompletos

print(f'->{dados_faltantes}')


#-------------------------------segunda parte---------------------------------------------------------------------------
verifica_type = df[['limite_credito', 'valor_transacoes_12m']].dtypes

# print(f'{verifica_type}')


fn = lambda valor: float(valor.replace('.', "").replace(',','.'))

teste_valores = ['12.691,51','1.144,90','8.256,96','1.291,45','3.418,56','1.887,72','3.313,03','1.171,56']
teste_fn = list(map(fn, teste_valores))

# print(teste_fn)


df['limite_credito'] = df['limite_credito'].apply(fn)
df['valor_transacoes_12m'] = df['valor_transacoes_12m'].apply(fn)

seilah = df[['limite_credito', 'valor_transacoes_12m']].head(n=5)
# print(f'{seilah}')

df.dropna(inplace=True) #elimina as linhas com dados faltantes
# print(df.shape)



seilah='-'
print(f'{seilah}')



# import matplotlib.pyplot as plt
# import seaborn as sns

# def plot_comparacao(dataframe, coluna, titulos):
#     eixo = 0
#     max_y = 0
#     max_freq = dataframe[coluna].value_counts().max() * 1.1  

#     fig, axes = plt.subplots(1, 3, figsize=(20, 5), sharex=True)

#     dataframes = [dataframe, dataframe[dataframe['default'] == 0], dataframe[dataframe['default'] == 1]]

#     for df, titulo in zip(dataframes, titulos):
#         df_to_plot = df[coluna].value_counts().to_frame().reset_index()
#         df_to_plot.columns = [coluna, 'frequencia_absoluta']
#         df_to_plot.sort_values(by=[coluna], inplace=True)

#         ax = sns.barplot(x=df_to_plot[coluna], y=df_to_plot['frequencia_absoluta'], ax=axes[eixo])
#         ax.set(title=titulo, xlabel=coluna.capitalize(), ylabel='Frequência Absoluta')
#         ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=90)
#         _, max_y_f = ax.get_ylim()
#         max_y = max_y_f if max_y_f > max_y else max_y
#         ax.set(ylim=(0, max_freq))

#         eixo += 1

#     plt.tight_layout()
#     plt.show()

#     def plot_histograms(dataframe, titulos, coluna):
#     figura, eixos = plt.subplots(1, 3, figsize=(20, 5), sharex=True)
#     max_y = 0
#     eixo = 0
    
#     dataframes = [dataframe, dataframe[dataframe['default'] == 0], dataframe[dataframe['default'] == 1]]

#     for df, titulo in zip(dataframes, titulos):
#         f = sns.histplot(x=coluna, data=df, stat='count', ax=eixos[eixo])
#         f.set(title=titulo, xlabel=coluna.capitalize(), ylabel='Frequência Absoluta')
#         _, max_y_f = f.get_ylim()
#         max_y = max_y_f if max_y_f > max_y else max_y
#         f.set(ylim=(0, max_y))
#         eixo += 1


#     plt.tight_layout()
#     plt.show()

# coluna = 'qtd_transacoes_12m'
# titulos = [
#     'Qtd. de Transações no Último Ano',
#     'Qtd. de Transações no Último Ano de Adimplentes',
#     'Qtd. de Transações no Último Ano de Inadimplentes'
# ]

# plot_histograms(df_sem_na, titulos, coluna)
# plot_comparacao(df_sem_na, coluna, titulos)

# coluna = 'escolaridade'
# titulos = [
#     'Escolaridade dos Clientes',
#     'Escolaridade dos Clientes Adimplentes',
#     'Escolaridade dos Clientes Inadimplentes'
# ]

# plot_histograms(df_sem_na, titulos, coluna)
# plot_comparacao(df_sem_na, coluna, titulos)

# coluna = 'salario_anual'
# titulos = [
#     'Salário Anual dos Clientes',
#     'Salário Anual dos Clientes Adimplentes',
#     'Salário Anual dos Clientes Inadimplentes'
# ]

# plot_histograms(df_sem_na, titulos, coluna)
# plot_comparacao(df_sem_na, coluna, titulos)

# f = sns.relplot(x='valor_transacoes_12m', y='qtd_transacoes_12m', data=df_sem_na, hue='default')

# _ = f.set(title='Relação entre Valor e Quantidade de Transações no Último Ano',
#           xlabel='Valor das Transações no Último Ano',
#           ylabel='Quantidade das Transações no Último Ano')

# plt.show()

