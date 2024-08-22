from funcao import *

nome = saudacao()

resposta = "sim"
resposta = resposta.lower()

while resposta == "sim":
    conversão = input(f"Qual conversão você deseja fazer {nome}?\nComprimento, Volume, Massa, Área ou Temperatura: ").lower()
    if conversão == "comprimento":
        comprimento()
        pass
    elif conversão == "volume":
        volume()
        pass
    elif conversão == "massa":
        massa()
        pass
    elif conversão == "temperatura":
        temperatura()
        pass
    elif conversão == "area":
        area()
        pass
    resp = input("Gostaria de fazer uma nova conversão?")
