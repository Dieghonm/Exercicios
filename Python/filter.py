### Exercícios Básicos

# 1. **Filtrando números pares**:
#    # Use a função filter() para criar uma lista apenas com os números pares de uma lista dada.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #    # Saída esperada: [2, 4, 6, 8, 10]

pares = filter(lambda x: not x%2 , numeros )
# print(list(pares))

# 2. **Filtrando strings que começam com uma letra específica**:
#    # Use filter() para retornar uma lista de palavras que começam com 'a'.
palavras = ["apple", "banana", "apricot", "cherry", "avocado"] #    # Saída esperada: ["apple", "apricot", "avocado"]

inicial = filter(lambda x: x[0] == 'a', palavras)
# print(list(inicial))

# 3. **Filtrando números negativos**:
#    # Use filter() para criar uma lista que contenha apenas números negativos.
numeros = [10, -1, -5, 3, -2, 0, 6, -7] #    # Saída esperada: [-1, -5, -2, -7]

negativos = filter(lambda x: x<0, numeros)
# print(list(negativos))

# ### Exercícios Intermediários

# 4. **Filtrando palavras com uma certa quantidade de letras**:
#    # Use filter() para retornar palavras com exatamente 5 letras.
palavras = ["hello", "world", "Python", "code", "filter"] #    # Saída esperada: ["hello", "world"]

letras5 = filter(lambda x: len(x) == 5, palavras)
# print(list(letras5))

# 5. **Filtrando números que são múltiplos de um número dado**:
#    # Use filter() para encontrar todos os múltiplos de 3 em uma lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #    # Saída esperada: [3, 6, 9, 12, 15]

multiplos3 = filter(lambda x:  not x%3, numeros)
# print(list(multiplos3))

# 6. **Filtrando strings que representam números**:
#    # Use filter() para filtrar apenas os elementos que são strings de números em uma lista mista.
misto = ["123", "hello", "456", "world", "789"] #    # Saída esperada: ["123", "456", "789"]

numero = filter(lambda x: x.isdigit(), misto)
# print(list(numero))

# ### Exercícios Avançados

# 7. **Filtrando palavras que são palíndromos**:
#    # Use filter() para retornar apenas as palavras que são palíndromos (lidas da mesma forma de trás 
# para frente).
palavras = ["madam", "racecar", "apple", "level", "hello"]
#    # Saída esperada: ["madam", "racecar", "level"]

palindromo = filter(lambda x: x==x[::-1] , palavras)
# print(list(palindromo))

# 8. **Filtrando dicionários por um valor de chave específico**:
#    # Use filter() para retornar uma lista de dicionários onde o valor da chave 'idade' é maior que 30.
pessoas = [
    {"nome": "Alice", "idade": 28},
    {"nome": "Bob", "idade": 35},
    {"nome": "Charlie", "idade": 32},
    {"nome": "David", "idade": 25}
]
#    # Saída esperada: [{"nome": "Bob", "idade": 35}, {"nome": "Charlie", "idade": 32}]

idade = filter(lambda x: x['idade'] > 30, pessoas)
# print(list(idade))

# 10. **Filtrando strings por comprimento**:
#     python
#     # Use filter() para retornar uma lista de strings que têm mais de 4 caracteres.
strings = ["hi", "hello", "yes", "no", "maybe", "Python"]
#     # Saída esperada: ["hello", "maybe", "Python"]
#     

string4 = filter(lambda x: len(x) > 4, strings)
print(list(string4))