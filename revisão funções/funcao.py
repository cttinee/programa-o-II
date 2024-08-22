def Saudacao():
    nome = input("Como gostaria de ser chamado? ").capitalize()
    if nome[-1] == "o":
        print(f"Seja muito bem vindo {nome}!!\n")
    else:
        print(f"Seja muito bem vinda {nome}!!\n")
    return nome

def Comprimento():
    print("Você escolheu a conversão de comprimento.")
    medida = input("Qual a medida da conversão?\nCentimetro(C):\nMetro(M):\nKilometro(K):/n").upper()
    medida_conversao = input("Para qual medida você quer converter?\nCentimetro(C):\nMetro(M):\nKilometro(K):/n").upper()
    valor = float(input("Digite o valor para converter:/n"))
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

def Volume():
    print("Você escolheu converter volume.")
    medida = input("Qual a medida da conversão?\nMililitro(M)\nLitro(L):").upper()
    medida_conversao = input("Para qual medida você quer converter?\nMililitro(M)\nLitro(L):").upper()
    valor = float(input("Digite o valor para converter:"))
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

def Massa():
    print("Você escolheu converter massa.")
    medida = input("Qual a medida da conversão?\nGrama(G)\nQuilograma(K)\nTonelada(T):").upper()
    medida_conversao = input("Para qual medida você quer converter?\nGrama(G)\nQuilograma(Q)\nTonelada(T):").upper()
    valor = float(input("Digite o valor para converter:"))
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

def Temperatura():
    print("Você escolheu converter temperatura.")
    medida = input("Qual a medida da conversão?\nCelsius(C)\nFahrenheit(F)\nKelvin(K):").upper()
    medida_conversao = input("Para qual medida você quer converter?\nCelsius(C)\nFahrenheit(F)\nKelvin(K):").upper()
    valor = float(input("Digite o valor para converter:"))
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

def Area():
    print("Você escolheu converter area.")
    medida = input("Qual a medida da conversão?\nCentímetro quadrado(C)\nMetro quadrado(M)\nHectare(H)").upper()
    medida_conversao = input("Para qual medida você quer converter?\n\nCentímetro quadrado(C)\nMetro quadrado(M)\nHectare(H)").upper()
    valor = float(input("Digite o valor para converter:"))
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

