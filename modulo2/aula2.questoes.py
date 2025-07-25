aula2.py
# ============================
# Questão 1
# ============================
print("Questão 1")

a = 5
b = 2

print("Tipo de a:", type(a))
print("Tipo de b:", type(b))

c = a / b

print("Valor de c:", c)
print("Tipo de c:", type(c))


# ============================
# Questão 2
# ============================
print("\nQuestão 2")

texto = "o resultado é"
num1 = 10
num2 = 3.5

resultado = num1 + num2

print("Texto:", texto)
print("Tipo:", type(texto))

print("Número 1:", num1)
print("Tipo:", type(num1))

print("Número 2:", num2)
print("Tipo:", type(num2))

print("Resultado:", resultado)
print("Tipo:", type(resultado))


# ============================
# Questão 3
# ============================
print("\nQuestão 3")

v1 = 10
v2 = 20

temp = v1
v1 = v2
v2 = temp

print("Novo valor de v1:", v1)
print("Novo valor de v2:", v2)


# ============================
# Questão 4
# ============================
print("\nQuestão 4")

saldo = 500.0
juros = 1.01

saldo = saldo * juros
saldo = saldo * juros
saldo = saldo * juros

print("Após 3 meses meu novo saldo é:", saldo)
