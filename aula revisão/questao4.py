data = input("Digite a data de nascimento dd/mm/aaaa:")
ano = int(data[6:])
mes = int(data[3:5])
dia = int(data[:2])

if ano % 4 == 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            print("Data válida.")
    elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            print("Data válida.")
    else: 
        print("Data inválida.")
else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            print("Data válida.")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <=30:
            print("Data válida.")
    elif mes ==2:
        if dia <= 29:
            print("Data válida.")
    else:
        print("Data inválida, tente novamente.")        