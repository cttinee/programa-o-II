# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número inteiro:"))

primo = True

if numero <= 1:
    primo = False 
else:
    for i in range( 2, int (numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")

