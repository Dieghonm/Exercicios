import csv
from sys import argv
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Verificar se pelo menos um argumento foi passado para o nome do arquivo de saída
if len(argv) < 2:
    print("Uso: python visualizacao.py <nome_do_arquivo>") #para salvar o grafico e necessario nomealo, e fazemos isso passando um nome apos a chamada no app no console    exit(1)

# Carregar os dados do CSV
df = pd.read_csv('./EBAC/Mpython10/taxa-cdi.csv')

# Configurar o gráfico
grafico = sns.lineplot(x='hora', y='taxa', data=df)

# Ajustar os rótulos do eixo x com rotação de 90 graus usando o Matplotlib
plt.xticks(rotation=90)

# Salvar o gráfico com o nome especificado no argumento
nome_arquivo = argv[1] + ".png"
grafico.get_figure().savefig(nome_arquivo)
print(f"Gráfico salvo como {nome_arquivo}")


