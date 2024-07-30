import os
dados = open("dados/dicionario_pessoas.xls")
print(dados)

print(f'Caminho Relativo: {os.path.relpath(dados.name)}')
print(f'Caminho Absoluto: {os.path.abspath(dados.name)}')

dados.close()

text = open('dados/pessoas_2015.txt')

conteudo1 = text.read()
# print(conteudo1)

conteudo2 = text.readline()
print(conteudo2)

conteudo3 = text.readlines()
# print(conteudo3)
print(type(conteudo3))

text.close()


with open("dados/novo", 'w') as novo:
    novo.write('Ola mundo!!')

novo = open('dados/novo')
print(novo.read())
novo.close()

stripMetodo = '01 23 456 789 987 435 654 a 123456789 a'
print(stripMetodo)
print(stripMetodo.strip('0123456789 '))

conteudo = "Python é uma linguagem de programação poderosa"
palavra = conteudo.split(" ")
print(palavra)

palavras = ['Python', 'é', 'uma', 'linguagem', 'poderosa']
frase = " ".join(palavras)
print(frase)

