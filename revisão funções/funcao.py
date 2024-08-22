def saudacao():
    nome = input("Olá! Como gostaria de ser chamado? ").capitalize()
        print(f"Seja bem vindo(a) {nome}!!\n")
    return nome

def comprimento():
    print("Você escolheu a conversão de comprimento.")
    medida = input("Qual a medida da conversão?\n Centimetro(C):\n Metro(M):\n Kilometro(K):/n").upper()
    medida_conversao = input("Para qual medida você quer converter?\n Centimetro(C):\n Metro(M):\n Kilometro(K):/n").upper()
    valor = float(input("Digite o valor que deseja converter:/n"))
    valor_convertido = 0
    if medida != medida_conversao:
        valor_convertido = 0
        if medida == "C" and medida_conversao == "M":
            valor_convertido = valor/100
        elif medida == "C" and medida_conversao == "K":
            valor_convertido = valor/100000
        elif medida == "M" and medida_conversao == "C":
            valor_convertido = valor*100
        elif medida == "M" and medida_conversao == "K":
            valor_convertido = valor/1000
        elif medida == "K" and medida_conversao == "M":
            valor_convertido = valor*1000
        elif medida == "K" and medida_conversao == "C":
            valor_convertido = valor*100000
    else:
        print("Medidas inválidas!")
    print(valor_convertido)

def volume():
    print("Você escolheu converter volume.")
    medida = input("Qual a medida da conversão?\n Mililitro(M)\n Litro(L):").upper()
    medida_conversao = input("Para qual medida você quer converter?\n Mililitro(M)\n Litro(L):").upper()
    valor = float(input("Digite o valor que deseja converter:"))
    valor_convertido = 0
    if medida != medida_conversao:
        valor_convertido = 0
        if medida == "L" and medida_conversao == "M":
            valor_convertido = valor*1000
        elif medida == "M" and medida_conversao == "L":
            valor_convertido = valor/1000
    else:
        print("Medidas inválidas!")
    print(valor_convertido)

def massa():
    print("Você escolheu converter massa.")
    medida = input("Qual a medida da conversão?\n Grama(G)\n Quilograma(K)\n Tonelada(T):").upper()
    medida_conversao = input("Para qual medida você quer converter?\n Grama(G)\n Quilograma(Q)\n Tonelada(T):").upper()
    valor = float(input("Digite o valor que deseja converter:"))
    valor_convertido = 0
    if medida != medida_conversao:
        valor_convertido = 0
        if medida == "G" and medida_conversao == "Q":
            valor_convertido = valor/1000
        elif medida == "G" and medida_conversao == "T":
            valor_convertido = valor/0.000001
        elif medida == "Q" and medida_conversao == "G":
            valor_convertido = valor*1000
        elif medida == "Q" and medida_conversao == "T":
            valor_convertido = valor/1000
        elif medida == "T" and medida_conversao == "G":
            valor_convertido = valor/1000000
        elif medida == "T" and medida_conversao == "Q":
            valor_convertido = valor/1000
    else:
        print("Medidas inválidas!")
    print(valor_convertido)

def temperatura():
    print("Você escolheu converter temperatura.")
    medida = input("Qual a medida da conversão?\n Celsius(C)\n Fahrenheit(F)\n Kelvin(K):").upper()
    medida_conversao = input("Para qual medida você quer converter?\n Celsius(C)\n Fahrenheit(F)\n Kelvin(K):").upper()
    valor = float(input("Digite o valor que deseja converter:"))
    if medida != medida_conversao:
        valor_convertido = 0
        if medida == "C" and medida_conversao == "F":
            valor_convertido = (valor*1.8)+32
        elif medida == "F" and medida_conversao == "C":
            valor_convertido = (valor-32)/1.8
        elif medida == "C" and medida_conversao == "K":
            valor_convertido = valor+273.15
        elif medida == "K" and medida_conversao == "C":
            valor_convertido = valor-273.15
    else:
        print("Medidas inválidas!")
    print(valor_convertido)

def area():
    print("Você escolheu converter área.")
    medida = input("Qual a medida da conversão?\n Centímetro quadrado(C)\n Metro quadrado(M)\n Hectare(H)").upper()
    medida_conversao = input("Para qual medida você quer converter?\n \nCentímetro quadrado(C)\n Metro quadrado(M)\n Hectare(H)").upper()
    valor = float(input("Digite o valor que deseja converter:"))
    if medida != medida_conversao:
        valor_convertido = 0
        if medida == "C" and medida_conversao == "M":
            valor_convertido = valor/10000
        elif medida == "M" and medida_conversao == "C":
            valor_convertido = valor*10000
        elif medida == "C" and medida_conversao == "H":
            valor_convertido = valor/100000000
        elif medida == "H" and medida_conversao == "C":
            valor_convertido = valor*100000000
        elif medida == "M" and medida_conversao == "H":
            valor_convertido = valor/10000

    else:
        print("Medidas inválidas!")
    print(valor_convertido)

