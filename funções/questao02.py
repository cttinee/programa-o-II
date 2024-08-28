# Faça um programa que calcule a área de um terreno e imprima na tela.

def area (largura, comprimento):
    area = largura * comprimento
    print(f"A área do terreno é {area} metros quadrados.")
    
largura = float(input("Digite a largura do terreno em metros:"))
comprimento = float(input("Digite o comprimento do terreno em metros:"))

area(largura, comprimento)
