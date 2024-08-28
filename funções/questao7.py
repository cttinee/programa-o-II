# Crie uma função que receba um número indeterminado de valores inteiros e
# depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):

def inteiros(numeros):
    soma = 0
    numero = [int(num) for num in numeros]
    for a in numero:
        soma += a
    print(f"A soma de todos numeros são de: {soma}")
    print(f"A lista somada foi de {numero}")

numero = input("DIgite varios numeros inteiros: ").split(",") #split é utilizado para a manipulação de strings.
inteiros(numero)
