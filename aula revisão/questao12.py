# Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

numeros = []

while True:
    try:
        N = int(input("Quantos números você deseja inserir? "))
        if N > 0:
            break
        else:
            print("O número deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

for i in range(N):
    while True:
        try:
            numero = float(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"\nO menor valor é: {menor}")
print(f"O maior valor é: {maior}")
print(f"A soma dos valores é: {soma:.2f}")
