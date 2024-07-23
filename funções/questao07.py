# Crie um programa de câmbio. 
# Nesse programa adicione funções que realizem conversões de real para dólar, real para euro 
# e real para peso argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
# 1,00 real = 0,18 dólar para Estados Unidos;
# 1,00 real = 0,16 euro para Portugal;
# 1,00 real = 0,0061 peso para Argentina;

def real_dolar(valor_real):
    taxa_dolar = 0.18
    valor_dolar = valor_real * taxa_dolar
    return valor_dolar

def real_euro(valor_real):
    taxa_euro = 0.16
    valor_euro = valor_real * taxa_euro
    return valor_euro

def real_peso(valor_real):
    taxa_peso = 0.0061
    valor_peso = valor_real * taxa_peso
    return valor_peso


print("Bem-vindo ao programa de conversão de câmbio!")
print("Opções disponíveis:")
print("1 - Real para Dólar.")
print("2 - Real para Euro.")
print("3 - Real para Peso Argentino")
escolha = int(input("Escolha o número que corresponde à conversão desejada:"))

valor_real = float(input("Digite o valor em real que deseja converter:"))

if escolha == 1:
    conversao = real_dolar(valor_real)
    print(f"R$ {valor_real:.2f} equivalem a $ {conversao:.2f} dólares americanos.")
elif escolha == 2:
    conversao = real_euro(valor_real)
    print(f"R$ {valor_real:.2f} equivalem a € {conversao:.2f} euros.")
elif escolha == 3:
    conversao = real_peso(valor_real)
    print(f"R$ {valor_real:.2f} equivalem a $ {conversao:.2f} pesos argentinos.")
else:
    print("Opção inválida. Escolha uma opção válida.")
