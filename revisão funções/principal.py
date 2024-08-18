from conversoes import (
    converter_comprimento,
    converter_volume,
    converter_massa,
    converter_temperatura,
    converter_area
)

def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao sistema de conversão.")

def selecionar_categoria():
    print("\nEscolha a categoria de conversão:")
    print("1. Comprimento")
    print("2. Volume")
    print("3. Massa")
    print("4. Temperatura")
    print("5. Área")
    escolha = input("Digite o número da categoria desejada: ")
    return escolha

def converter_unidade(categoria):
    if categoria == '1':
        print("\nEscolha a unidade de comprimento:")
        print("1. Centímetro")
        print("2. Metro")
        print("3. Quilômetro")
        unidades = {"1": "cm", "2": "m", "3": "km"}
        de = input("De (número da unidade de origem): ").strip()
        para = input("Para (número da unidade de destino): ").strip()
        valor = float(input("Digite o valor a ser convertido: "))
        try:
            unidade_de = unidades.get(de)
            unidade_para = unidades.get(para)
            if unidade_de is None or unidade_para is None:
                raise ValueError("Unidade inválida fornecida.")
            resultado = converter_comprimento(valor, unidade_de, unidade_para)
            print(f"Resultado: {resultado:.2f} {unidade_para}")
        except ValueError as e:
            print(e)
    
    elif categoria == '2':
        print("\nEscolha a unidade de volume:")
        print("1. Mililitro")
        print("2. Litro")
        unidades = {"1": "ml", "2": "l"}
        de = input("De (número da unidade de origem): ").strip()
        para = input("Para (número da unidade de destino): ").strip()
        valor = float(input("Digite o valor a ser convertido: "))
        try:
            unidade_de = unidades.get(de)
            unidade_para = unidades.get(para)
            if unidade_de is None or unidade_para is None:
                raise ValueError("Unidade inválida fornecida.")
            resultado = converter_volume(valor, unidade_de, unidade_para)
            print(f"Resultado: {resultado:.2f} {unidade_para}")
        except ValueError as e:
            print(e)
    
    elif categoria == '3':
        print("\nEscolha a unidade de massa:")
        print("1. Grama")
        print("2. Kilograma")
        print("3. Tonelada")
        unidades = {"1": "g", "2": "kg", "3": "t"}
        de = input("De (número da unidade de origem): ").strip()
        para = input("Para (número da unidade de destino): ").strip()
        valor = float(input("Digite o valor a ser convertido: "))
        try:
            unidade_de = unidades.get(de)
            unidade_para = unidades.get(para)
            if unidade_de is None or unidade_para is None:
                raise ValueError("Unidade inválida fornecida.")
            resultado = converter_massa(valor, unidade_de, unidade_para)
            print(f"Resultado: {resultado:.2f} {unidade_para}")
        except ValueError as e:
            print(e)
    
    elif categoria == '4':
        print("\nEscolha a unidade de temperatura:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        unidades = {"1": "C", "2": "F", "3": "K"}
        de = input("De (número da unidade de origem): ").strip()
        para = input("Para (número da unidade de destino): ").strip()
        valor = float(input("Digite o valor a ser convertido: "))
        try:
            unidade_de = unidades.get(de)
            unidade_para = unidades.get(para)
            if unidade_de is None or unidade_para is None:
                raise ValueError("Unidade inválida fornecida.")
            resultado = converter_temperatura(valor, unidade_de, unidade_para)
            print(f"Resultado: {resultado:.2f} {unidade_para}")
        except ValueError as e:
            print(e)
    
    elif categoria == '5':
        print("\nEscolha a unidade de área:")
        print("1. Centímetro quadrado")
        print("2. Metro quadrado")
        print("3. Hectare")
        unidades = {"1": "cm2", "2": "m2", "3": "ha"}
        de = input("De (número da unidade de origem): ").strip()
        para = input("Para (número da unidade de destino): ").strip()
        valor = float(input("Digite o valor a ser convertido: "))
        try:
            unidade_de = unidades.get(de)
            unidade_para = unidades.get(para)
            if unidade_de is None or unidade_para is None:
                raise ValueError("Unidade inválida fornecida.")
            resultado = converter_area(valor, unidade_de, unidade_para)
            print(f"Resultado: {resultado:.2f} {unidade_para}")
        except ValueError as e:
            print(e)
    
    else:
        print("Categoria inválida.")

def main():
    nome = input("Digite seu nome: ")
    saudacao(nome)

    while True:
        categoria = selecionar_categoria()
        converter_unidade(categoria)
        continuar = input(f"\n{nome}, deseja realizar outra conversão? (sim/não): ").strip().lower()
        if continuar != 'sim':
            print(f"Até mais, {nome}!")
            break

if __name__ == '__main__':
    main()
