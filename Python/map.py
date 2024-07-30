# ## Nível 1: Básico
# ### **Exercício 1: Converter uma lista de números em seus quadrados**
# **Descrição**: Dada uma lista de números `[1, 2, 3, 4, 5]`, use `map()` 
# para retornar uma lista de seus quadrados.

numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda num: num**2, numeros)
# print(list(quadrados))


# ### **Exercício 2: Converter uma lista de strings para maiúsculas**
# **Descrição**: Dada uma lista de palavras `['python', 'map', 'lambda']`, use `map()` 
# para retornar uma lista com todas as palavras em maiúsculas.

lista = ['python', 'map', 'lambda']
upper = map(lambda text: text.upper(), lista)
# print(list(upper))


# ## Nível 2: Intermediário
# ### **Exercício 3: Somar valores de duas listas**
# **Descrição**: Dadas duas listas `[1, 2, 3]` e `[4, 5, 6]`, use `map()` para retornar uma 
# lista com a soma dos elementos correspondentes.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sumList = map(lambda item1, item2: item1 + item2, list1, list2)
# print(list(sumList))


# ### **Exercício 4: Extrair os comprimentos de uma lista de palavras**
# **Descrição**: Dada uma lista de palavras `['Python', 'é', 'ótimo']`, use `map()` para retornar 
# uma lista com o comprimento de cada palavra.

palavras = ['Python', 'é', 'ótimo']
palavrasLenght = map(lambda palavra : len(palavra), palavras)
# print(list(palavrasLenght))


# ## Nível 3: Avançado
# ### **Exercício 5: Calcular o preço com desconto**
# **Descrição**: Dada uma lista de preços `[100, 200, 300]` e uma lista de descontos `[10, 20, 15]` 
# (em porcentagem), use `map()` para calcular o preço final após aplicar o desconto.

preços = [100, 200, 300]
descontos = [10, 20, 15]
PFinal = map(lambda preço, desconto: preço - (preço*(desconto/100)) , preços, descontos)
# print(list(PFinal))


# ### **Exercício 6: Converter temperaturas de Celsius para Fahrenheit**
# **Descrição**: Dada uma lista de temperaturas em Celsius `[0, 20, 37, 100]`, use `map()` para 
# converter essas temperaturas para Fahrenheit usando a fórmula `F = C * 9/5 + 32`.

temperatura = [0, 20, 37, 100]
Fahrenheit = map(lambda temp: temp * 9/5 + 32 ,temperatura)
# print(list(Fahrenheit))


# ## Nível 4: Desafios
# ### **Exercício 7: Formatar números como strings de moeda**
# **Descrição**: Dada uma lista de números `[1234.567, 89.0, 6789]`, use `map()` para formatar cada 
# número como uma string de moeda com duas casas decimais (por exemplo, `1234.57`).


numeros = [1234.567, 89.0, 6789]
moeda = map(lambda val: f'R${round(val, 2):.2f}', numeros)  #${x:.2f}
# print(list(moeda))


# ### **Exercício 8: Concatenar duas listas de strings**
# **Descrição**: Dadas duas listas de strings `['a', 'b', 'c']` e `['x', 'y', 'z']`, use `map()` para 
# retornar uma lista de concatenações dos elementos correspondentes (por exemplo, `'ax'`).

list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']
list3 = map(lambda a, b: a+b, list1, list2 )
# print(list(list3))


# ### **Exercício 9: Remover espaços de uma lista de strings**
# **Descrição**: Dada uma lista de strings `['  Python  ', ' map ', ' lambda ']`, use `map()` para 
# retornar uma lista com espaços removidos de cada string.

lista = ['  Python  ', ' map ', ' lambda ']
retorno = map(lambda palavra: palavra.strip(), lista)
# print(list(retorno))


# ### **Exercício 10: Criar dicionário a partir de duas listas**
# **Descrição**: Dadas duas listas `['nome', 'idade']` e `['Alice', 30]`, use `map()` para criar 
# um dicionário que combine essas listas em pares chave-valor.

list1 = ['nome', 'idade']
list2 = ['Alice', 30]
retorno = map(lambda key, value: (key, value), list1, list2)

# print(list(retorno))
teste = map(lambda x: type(x), retorno)
print(list(teste))