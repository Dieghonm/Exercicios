# ### Exercícios Básicos

# 1. **Criando uma classe simples**:
#    - **Tarefa**: Crie uma classe `Pessoa` com os atributos `nome` e `idade`.
#  Crie um método `mostrar_informacoes` que exiba o nome e a idade da pessoa.

class pessoa:
  def __init__(self, nome: str, idade: int):
    self.nome = nome
    self.idade = idade

  def mostrar_informacoes(self):
    return f"Nome: {self.nome}, Idade: {self.idade}"

pessoa = pessoa('ligia', 30)
# print(pessoa.mostrar_informacoes())


# 2. **Classe com método modificador**:
#    - **Tarefa**: Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo`.
#  Adicione métodos `depositar` e `sacar` que modifiquem o saldo da conta.

class ContaBancaria:
  def __init__(self, titular : str, saldo: float):
    self.titular = titular
    self.saldo = saldo
  
  def depositar(self, deposito:float):
    self.saldo = self.saldo + deposito

  def sacar(self, saque: float):
    self.saldo = self.saldo - saque

  def extrato(self):
    return f"titular: {self.titular}, saldo: {self.saldo}"
  
cliente = ContaBancaria('diegho', 1000)
# print(cliente.extrato())
cliente.sacar(500)
# print(cliente.extrato())
cliente.depositar(1000)
# print(cliente.extrato())

# 3. **Herança básica**:
#    - **Tarefa**: Crie uma classe `Veiculo` com um método `mover`. 
# Crie subclasses `Carro` e `Bicicleta` que herdem de `Veiculo` e substituam o método `mover` 
# com mensagens apropriadas.

class veiculo:
  def mover(self):
    pass

class Carro(veiculo):
  def mover(self):
    return "O carro está se movendo"

class Bicicleta(veiculo):
  def mover(self):
    return "A bicicleta está se movendo"

carro = Carro()
bicicleta = Bicicleta()
# print(carro.mover())
# print(bicicleta.mover())


# ### Exercícios Intermediários

# 4. **Encapsulamento**:
#    - **Tarefa**: Crie uma classe `Produto` com os atributos `nome` e `preco`. Torne `preco` um atributo
#  privado e adicione métodos getter e setter para ele.

class Produto:
  def __init__ (self, nome:str, preco:float):
    self.nome = nome
    self.__preco = preco

  def get_preco(self):
    return self.__preco

  def set_preco(self, novo_preco: float):
    self.__preco = novo_preco

  def informacoes(self):
    return f"Produto: {self.nome}, Preço: {self.get_preco()}"

produto = Produto("Café", 10)
produto.set_preco(15)
# print(produto.informacoes())


# 5. **Métodos estáticos**:
#    - **Tarefa**: Crie uma classe `Calculadora` com métodos estáticos `somar`, `subtrair`, `multiplicar`,
#  e `dividir`.

class Calculadora:
  def somar(valor : float, valor2:float):
    return valor + valor2
  def subtrair(valor : float, valor2:float):
    return valor - valor2
  def multiplicar(valor : float, valor2:float):
    return valor * valor2
  def dividir(valor : float, valor2:float):
    return valor / valor2

# print(Calculadora.somar(10, 5))
# print(Calculadora.subtrair(10, 5))
# print(Calculadora.multiplicar(10, 5))
# print(Calculadora.dividir(10, 5))

# 6. **Herança e Polimorfismo**:
#    - **Tarefa**: Crie uma classe base `Animal` com um método `fazer_som`. Crie subclasses `Cachorro` 
# e `Gato` que implementam `fazer_som`.

class Animal:
  def __init__(self):
    pass
  def fazer_som(self):
   pass

class Cachorro(Animal):
  def fazer_som(self):
    return "Au au!"

class Gato(Animal):
  def fazer_som(self):
    return "Miau!"

animais = [Cachorro(), Gato()]
# for animal in animais:
#     print(animal.fazer_som())  


# 7. **Classe abstrata**:
#    - **Tarefa**: Use o módulo `abc` para criar uma classe abstrata `Forma` com o método abstrato 
# `area`. Implemente `Retangulo` e `Circulo`.

from abc import ABC, abstractmethod

class Forma(ABC):
  @abstractmethod
  def area(self):
    pass

class Retangulo(Forma):
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

  def area(self):
    return self.largura * self.altura

class Circulo(Forma):
  def __init__(self, raio):
    self.raio = raio

  def area(self):
    return 3.14 * self.raio ** 2

formas = [Retangulo(3, 4), Circulo(5)]
for forma in formas:
  print(forma.area())


# ### Exercícios Avançados

# 8. **Composição de Objetos**:
#    - **Tarefa**: Crie uma classe `Motor` e uma classe `Carro` que possua um motor. Implemente métodos para ligar e desligar o motor.
#    ```python
#    class Motor:
#        def __init__(self):
#            self.ligado = False

#        def ligar(self):
#            self.ligado = True

#        def desligar(self):
#            self.ligado = False

#    class Carro:
#        def __init__(self, modelo):
#            self.modelo = modelo
#            self.motor = Motor()

#        def ligar_carro(self):
#            self.motor.ligar()

#        def desligar_carro(self):
#            self.motor.desligar()

#        def estado_carro(self):
#            return f"Carro: {self.modelo}, Motor {'Ligado' if self.motor.ligado else 'Desligado'}"

#    # Teste
#    carro = Carro("Fusca")
#    carro.ligar_carro()
#    print(carro.estado_carro())  # Saída esperada: "Carro: Fusca, Motor Ligado"
#    ```

# 9. **Gestão de Funcionários com Herança e Polimorfismo**:
#    - **Tarefa**: Crie uma classe base `Funcionario` e subclasses `Gerente` e `Desenvolvedor`. Implemente métodos específicos para cada classe.
#    ```python
#    class Funcionario:
#        def __init__(self, nome, salario):
#            self.nome = nome
#            self.salario = salario

#        def detalhes(self):
#            return f"Nome: {self.nome}, Salário: {self.salario}"

#    class Gerente(Funcionario):
#        def __init__(self, nome, salario, equipe):
#            super().__init__(nome, salario)
#            self.equipe = equipe

#        def detalhes(self):
#            return super().detalhes() + f", Equipe: {', '.join([membro.nome for membro in self.equipe])}"

#    class Desenvolvedor(Funcionario):
#        def __init__(self, nome, salario, linguagem):
#            super().__init__(nome, salario)
#            self.linguagem = linguagem

#        def detalhes(self):
#            return super().detalhes() + f", Linguagem: {self.linguagem}"

#    # Teste
#    dev1 = Desenvolvedor("Alice", 5000, "Python")
#    dev2 = Desenvolvedor

# ("Bob", 6000, "Java")
#    gerente = Gerente("Carol", 10000, [dev1, dev2])
#    print(gerente.detalhes())  # Saída esperada: "Nome: Carol, Salário: 10000, Equipe: Alice, Bob"
#    ```

# 10. **Sistema de Biblioteca**:
#     - **Tarefa**: Crie um sistema de biblioteca com classes `Livro`, `Usuario`, e `Biblioteca`. Implemente métodos para emprestar e devolver livros.
#     ```python
#     class Livro:
#         def __init__(self, titulo, autor):
#             self.titulo = titulo
#             self.autor = autor
#             self.emprestado = False

#     class Usuario:
#         def __init__(self, nome):
#             self.nome = nome
#             self.livros = []

#         def emprestar_livro(self, livro):
#             if not livro.emprestado:
#                 self.livros.append(livro)
#                 livro.emprestado = True
#             else:
#                 print("Livro já emprestado")

#         def devolver_livro(self, livro):
#             if livro in self.livros:
#                 self.livros.remove(livro)
#                 livro.emprestado = False
#             else:
#                 print("Livro não foi emprestado por este usuário")

#     class Biblioteca:
#         def __init__(self):
#             self.livros = []

#         def adicionar_livro(self, livro):
#             self.livros.append(livro)

#         def listar_livros(self):
#             return [f"{livro.titulo} por {livro.autor}" for livro in self.livros if not livro.emprestado]

#     # Teste
#     livro1 = Livro("1984", "George Orwell")
#     livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
#     usuario = Usuario("Diana")
#     biblioteca = Biblioteca()
#     biblioteca.adicionar_livro(livro1)
#     biblioteca.adicionar_livro(livro2)
#     usuario.emprestar_livro(livro1)
#     print(biblioteca.listar_livros())  # Saída esperada: ["O Senhor dos Anéis por J.R.R. Tolkien"]
#     ```

# ### Exercícios Avançados Extras

# 11. **Sistema de Gerenciamento de Reservas de Hotel**:
#     - **Tarefa**: Crie um sistema de reservas de hotel com classes `Quarto`, `Reserva`, `Cliente`, e `Hotel`. Implemente métodos para fazer e cancelar reservas.
#     ```python
#     from datetime import datetime

#     class Quarto:
#         def __init__(self, numero, tipo):
#             self.numero = numero
#             self.tipo = tipo
#             self.reservas = []

#     class Reserva:
#         def __init__(self, cliente, quarto, data_inicio, data_fim):
#             self.cliente = cliente
#             self.quarto = quarto
#             self.data_inicio = data_inicio
#             self.data_fim = data_fim

#     class Cliente:
#         def __init__(self, nome):
#             self.nome = nome
#             self.reservas = []

#     class Hotel:
#         def __init__(self, nome):
#             self.nome = nome
#             self.quartos = []

#         def adicionar_quarto(self, quarto):
#             self.quartos.append(quarto)

#         def fazer_reserva(self, cliente, numero_quarto, data_inicio, data_fim):
#             quarto = next((q for q in self.quartos if q.numero == numero_quarto), None)
#             if quarto:
#                 reserva = Reserva(cliente, quarto, data_inicio, data_fim)
#                 quarto.reservas.append(reserva)
#                 cliente.reservas.append(reserva)
#                 return reserva
#             return None

#         def listar_reservas(self):
#             reservas = []
#             for quarto in self.quartos:
#                 for reserva in quarto.reservas:
#                     reservas.append(f"Cliente: {reserva.cliente.nome}, Quarto: {reserva.quarto.numero}, "
#                                     f"Data: {reserva.data_inicio} - {reserva.data_fim}")
#             return reservas

#     # Teste
#     hotel = Hotel("Hotel Luxo")
#     quarto1 = Quarto(101, "Simples")
#     quarto2 = Quarto(102, "Luxo")
#     hotel.adicionar_quarto(quarto1)
#     hotel.adicionar_quarto(quarto2)
#     cliente = Cliente("Carlos")
#     hotel.fazer_reserva(cliente, 101, datetime(2024, 6, 1), datetime(2024, 6, 5))
#     print(hotel.listar_reservas())  # Saída esperada: ["Cliente: Carlos, Quarto: 101, Data: 2024-06-01 00:00:00 - 2024-06-05 00:00:00"]
#     ```

# 12. **Sistema de Gerenciamento de Estoque**:
#     - **Tarefa**: Crie um sistema de gerenciamento de estoque com classes `Produto`, `Fornecedor`, `Estoque`, e `Pedido`. Implemente métodos para adicionar produtos, registrar fornecedores e realizar pedidos.
#     ```python
#     class Produto:
#         def __init__(self, nome, preco):
#             self.nome = nome
#             self.preco = preco
#             self.quantidade = 0

#     class Fornecedor:
#         def __init__(self, nome):
#             self.nome = nome
#             self.produtos = []

#         def adicionar_produto(self, produto):
#             self.produtos.append(produto)

#     class Estoque:
#         def __init__(self):
#             self.produtos = {}

#         def adicionar_produto(self, produto, quantidade):
#             if produto.nome in self.produtos:
#                 self.produtos[produto.nome] += quantidade
#             else:
#                 self.produtos[produto.nome] = quantidade

#         def verificar_estoque(self, produto_nome):
#             return self.produtos.get(produto_nome, 0)

#     class Pedido:
#         def __init__(self, fornecedor, produto, quantidade):
#             self.fornecedor = fornecedor
#             self.produto = produto
#             self.quantidade = quantidade

#         def realizar_pedido(self, estoque):
#             estoque.adicionar_produto(self.produto, self.quantidade)

#     # Teste
#     estoque = Estoque()
#     fornecedor = Fornecedor("Fornecedor X")
#     produto = Produto("Notebook", 1500)
#     fornecedor.adicionar_produto(produto)
#     pedido = Pedido(fornecedor, produto, 10)
#     pedido.realizar_pedido(estoque)
#     print(estoque.verificar_estoque("Notebook"))  # Saída esperada: 10
#     ```

# ### Dicas para Avançar

# 1. **Padrões de Projeto**: Aprenda sobre e implemente padrões de projeto como Singleton, Factory, e Strategy.
# 2. **Interface e Polimorfismo**: Explore mais a fundo o uso de interfaces e polimorfismo em projetos complexos.
# 3. **Sistemas Reais**: Tente construir pequenos sistemas reais, como um sistema de gerenciamento de tarefas, um sistema de votação, ou uma plataforma de e-commerce simplificada.