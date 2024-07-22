# 1 - Defina uma função soma() que recebe dois números como parâmetros e calcula a soma entre eles.
# 2 - Defina uma função subtração() que recebe dois números como parâmetros e calcula a diferença entre eles.
# 3 - Agora faça uma função calculadora() que recebe dois números como parâmetros e retorna o resultado da soma e da subtração entre eles.
# 4 - Por fim, acresente funções para divisão e multiplicação nessa calculadora e chame a função calculadora.

def soma(valor1, valor2):
    resultado = valor1 + valor2
    print(resultado)

def subtracao(valor1, valor2):
    resultado = valor1 - valor2
    print(resultado)

def divisao (valor1, valor2):
    resultado = valor1 / valor2
    print(resultado)

def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    print(resultado)

def calculadora():
    pergunta1 = int(input("Digite um valor:"))
    pergunta2 = int(input("Digite um outro valor:"))
    soma(pergunta1, pergunta2)
    subtracao(pergunta1, pergunta2)
    divisao(pergunta1, pergunta2)
    multiplicacao(pergunta1, pergunta2)
calculadora()





