# Define as funções de cálculo
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Mostra as opções ao usuário
print("Escolha a operação desejada:")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

# Lê a escolha do usuário
opcao = int(input("Opção: "))

# Lê os valores de entrada
a = float(input("Valor 1: "))
b = float(input("Valor 2: "))

# Realiza o cálculo de acordo com a escolha do usuário
if opcao == 1:
    resultado = soma(a, b)
elif opcao == 2:
    resultado = subtracao(a, b)
elif opcao == 3:
    resultado = multiplicacao(a, b)
elif opcao == 4:
    resultado = divisao(a, b)
else:
    resultado = "Opção inválida!"

# Mostra o resultado
print(f"Resultado: {resultado}")
