from functools import reduce

# ### Exercícios Básicos

# 1. **Somando todos os números em uma lista**:
#    ```python
#    from functools import reduce

#    numeros = [1, 2, 3, 4, 5]
#    # Use reduce para somar todos os números
#    # Saída esperada: 15
#    ```

# 2. **Concatenando uma lista de strings**:
#    ```python
#    from functools import reduce

#    palavras = ["Hello", " ", "World", "!"]
#    # Use reduce para concatenar todas as strings
#    # Saída esperada: "Hello World!"
#    ```

# 3. **Encontrando o maior número em uma lista**:
#    ```python
#    from functools import reduce

#    numeros = [5, 1, 8, 3, 9, 2]
#    # Use reduce para encontrar o maior número
#    # Saída esperada: 9
#    ```

# ### Exercícios Intermediários

# 4. **Calculando o produto de todos os números em uma lista**:
#    ```python
#    from functools import reduce

#    numeros = [2, 3, 4]
#    # Use reduce para calcular o produto de todos os números
#    # Saída esperada: 24
#    ```

# 5. **Concatenando uma lista de listas em uma única lista**:
#    ```python
#    from functools import reduce

#    listas = [[1, 2], [3, 4], [5, 6]]
#    # Use reduce para concatenar todas as listas em uma única lista
#    # Saída esperada: [1, 2, 3, 4, 5, 6]
#    ```

# 6. **Contando o número de ocorrências de um caractere em uma string**:
#    ```python
#    from functools import reduce

#    frase = "banana"
#    # Use reduce para contar quantas vezes o caractere 'a' aparece na frase
#    # Saída esperada: 3
#    ```

# ### Exercícios Avançados

# 7. **Calculando o máximo divisor comum (MDC) de uma lista de números**:
#    ```python
#    from functools import reduce
#    import math

#    numeros = [24, 36, 48]
#    # Use reduce e math.gcd para calcular o MDC
#    # Saída esperada: 12
#    ```

# 8. **Filtrando os elementos duplicados em uma lista mantendo a ordem**:
#    ```python
#    from functools import reduce

#    numeros = [1, 2, 2, 3, 4, 3, 5, 1, 6]
#    # Use reduce para filtrar os duplicados e manter a ordem
#    # Saída esperada: [1, 2, 3, 4, 5, 6]
#    ```

# 9. **Calculando a soma dos dígitos de um número**:
#    ```python
#    from functools import reduce

#    numero = 12345
#    # Use reduce para calcular a soma dos dígitos
#    # Saída esperada: 15
#    ```

# 10. **Convertendo uma lista de binários em um número decimal**:
#     ```python
#     from functools import reduce

#     binarios = [1, 0, 1, 1]  # Representa o binário 1011
#     # Use reduce para converter para decimal
#     # Saída esperada: 11
#     ```

# ### Dicas de Implementação

# Para usar `reduce()`, você precisa definir uma função que toma dois argumentos e retorna um valor que será acumulado. Aqui estão alguns exemplos de como implementar alguns dos exercícios.

# #### Exercício 1: Somando todos os números

# ```python
# from functools import reduce

# numeros = [1, 2, 3, 4, 5]
# soma = reduce(lambda a, b: a + b, numeros)
# print(soma)  # Saída: 15
# ```

# #### Exercício 4: Calculando o produto

# ```python
# from functools import reduce

# numeros = [2, 3, 4]
# produto = reduce(lambda a, b: a * b, numeros)
# print(produto)  # Saída: 24
# ```

# #### Exercício 8: Filtrando duplicados

# ```python
# from functools import reduce

# numeros = [1, 2, 2, 3, 4, 3, 5, 1, 6]
# unicos = reduce(lambda acc, x: acc + [x] if x not in acc else acc, numeros, [])
# print(unicos)  # Saída: [1, 2, 3, 4, 5, 6]
# ```

# #### Exercício 10: Convertendo binário para decimal

# ```python
# from functools import reduce

# binarios = [1, 0, 1, 1]
# decimal = reduce(lambda acc, x: acc * 2 + x, binarios)
# print(decimal)  # Saída: 11
# ```

# ### Explicação dos Exercícios Avançados

# #### Exercício 7: Máximo Divisor Comum (MDC)

# ```python
# from functools import reduce
# import math

# numeros = [24, 36, 48]
# mdc = reduce(math.gcd, numeros)
# print(mdc)  # Saída: 12
# ```

# - **`reduce(math.gcd, numeros)`**: Aplica a função `math.gcd` cumulativamente à lista de números para encontrar o MDC.

# #### Exercício 9: Soma dos Dígitos

# ```python
# from functools import reduce

# numero = 12345
# soma_digitos = reduce(lambda acc, x: acc + int(x), str(numero), 0)
# print(soma_digitos)  # Saída: 15
# ```

# - **`reduce(lambda acc, x: acc + int(x), str(numero), 0)`**: Converte o número para string, depois aplica `reduce` para somar cada dígito.

# Esses exercícios devem ajudá-lo a praticar o uso da função `reduce()` em várias situações!