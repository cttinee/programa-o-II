# Faça um programa que receba três números do usuário, e identifique o maior
# através de uma função e o menor número através de outra função.

def num_maior(numero1, numero2, numero3):
    maior = max(numero1, numero2, numero3)
    return maior

def num_menor( numero1, numero2, numero3):
    menor = min (numero1, numero2, numero3)
    return menor

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maiornumero = num_maior(numero1, numero2, numero3)
menornumero = num_menor(numero1, numero2, numero3)

print(f"O maior número é: {maiornumero}")
print(f"O menor número é: {menornumero}")
