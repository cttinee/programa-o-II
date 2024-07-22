# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

while True:
    try:
        numero2 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

inicio = min(numero1, numero2)
fim = max(numero1, numero2)

print(f"Números inteiros no intervalo de {inicio} a {fim} (excluindo {inicio} e {fim}):")

for numero in range(inicio + 1, fim):
    print(numero)

