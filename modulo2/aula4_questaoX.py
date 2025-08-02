# Lê o comprimento do terreno em metros (inteiro)
comprimento = int(input("Digite o comprimento do terreno (m): "))

# Lê a largura do terreno em metros (inteiro)
largura = int(input("Digite a largura do terreno (m): "))

# Lê o preço por metro quadrado (ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Exibe o resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
# Lê a temperatura em Fahrenheit (inteiro)
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte para Celsius
celsius = int((fahrenheit - 32) * (5 / 9))

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
# Produto 1
nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
qtd1 = int(input("Digite a quantidade do produto 1: "))

# Produto 2
nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
qtd2 = int(input("Digite a quantidade do produto 2: "))

# Produto 3
nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
qtd3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o total
total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)

# Exibe o total formatado com separador de milhar e 2 casas decimais
print(f"Total: R${total:,.2f}")
# Lê o valor em reais
valor = int(input())

# Calcula cada tipo de nota usando divisão inteira
notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

notas5 = valor // 5
valor %= 5

notas2 = valor // 2
valor %= 2

notas1 = valor

# Exibe a quantidade de notas
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")
