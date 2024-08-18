# conversoes.py

def converter_comprimento(valor, de, para):
    unidades_comprimento = {
        "cm": 0.01,  # Centímetro para metro
        "m": 1,      # Metro
        "km": 1000   # Quilômetro para metro
    }
    
    if de not in unidades_comprimento or para not in unidades_comprimento:
        raise ValueError("Unidade inválida fornecida.")
    
    valor_em_metros = valor * unidades_comprimento[de]
    valor_convertido = valor_em_metros / unidades_comprimento[para]
    return valor_convertido

def converter_volume(valor, de, para):
    unidades_volume = {
        "ml": 0.001,  # Mililitro para litro
        "l": 1        # Litro
    }
    
    if de not in unidades_volume or para not in unidades_volume:
        raise ValueError("Unidade inválida fornecida.")
    
    valor_em_litros = valor * unidades_volume[de]
    valor_convertido = valor_em_litros / unidades_volume[para]
    return valor_convertido

def converter_massa(valor, de, para):
    unidades_massa = {
        "g": 0.001,  # Grama para quilograma
        "kg": 1,     # Quilograma
        "t": 1000    # Tonelada para quilograma
    }
    
    if de not in unidades_massa or para not in unidades_massa:
        raise ValueError("Unidade inválida fornecida.")
    
    valor_em_quilogramas = valor * unidades_massa[de]
    valor_convertido = valor_em_quilogramas / unidades_massa[para]
    return valor_convertido

def converter_temperatura(valor, de, para):
    if de == "C":
        if para == "F":
            return valor * 9/5 + 32
        elif para == "K":
            return valor + 273.15
        elif para == "C":
            return valor
        else:
            raise ValueError("Unidade inválida fornecida.")
    elif de == "F":
        if para == "C":
            return (valor - 32) * 5/9
        elif para == "K":
            return (valor - 32) * 5/9 + 273.15
        elif para == "F":
            return valor
        else:
            raise ValueError("Unidade inválida fornecida.")
    elif de == "K":
        if para == "C":
            return valor - 273.15
        elif para == "F":
            return (valor - 273.15) * 9/5 + 32
        elif para == "K":
            return valor
        else:
            raise ValueError("Unidade inválida fornecida.")
    else:
        raise ValueError("Unidade inválida fornecida.")

def converter_area(valor, de, para):
    unidades_area = {
        "cm2": 0.0001,  # Centímetro quadrado para metro quadrado
        "m2": 1,        # Metro quadrado
        "ha": 10000     # Hectare para metro quadrado
    }
    
    if de not in unidades_area or para not in unidades_area:
        raise ValueError("Unidade inválida fornecida.")
    
    valor_em_metros_quadrados = valor * unidades_area[de]
    valor_convertido = valor_em_metros_quadrados / unidades_area[para]
    return valor_convertido
