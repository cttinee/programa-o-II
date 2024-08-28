# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para personalizar a saída.

def converter_12h(hora, minuto):
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        return "Hora inválida"

    periodo = "A.M."
    if hora >= 12:
        periodo = "P.M."
    
    if hora == 0:
        hora_12h = 12
    elif hora > 12:
        hora_12h = hora - 12
    else:
        hora_12h = hora
    
    return hora_12h, minuto, periodo

def saida(hora_12h, minuto, periodo):
    return f"{hora_12h}:{minuto:02d} {periodo}"

hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))

hora_12h, minuto, periodo = converter_12h(hora, minuto)


saida_formatada= saida(hora_12h, minuto, periodo)
print(f"A hora convertida é: {saida_formatada}")
