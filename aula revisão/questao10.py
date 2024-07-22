# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Digite seu nome (mais de 3 caracteres): ").strip()
    if len(nome) > 3:
        break
    else:
        print("Nome inválido. O nome deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade (entre 0 e 150): ").strip())
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. A idade deve estar entre 0 e 150.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro para a idade.")


while True:
    try:
        salario = float(input("Digite seu salário (maior que 0): ").strip())
        if salario > 0:
            break
        else:
            print("Salário inválido. O salário deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para o salário.")

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").strip().lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo inválido. Por favor, digite 'f' ou 'm'.")

sexo_descricao = 'Feminino' if sexo == 'f' else 'Masculino'

while True:
    estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado,"
                          "'v' para viúvo, 'd' para divorciado): ").strip().lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido. Por favor, digite 's', 'c', 'v' ou 'd'.")

estado_civil_descricao = (
    'Solteiro' if estado_civil == 's' 
    else 'Casado' if estado_civil == 'c' 
    else 'Viúvo' if estado_civil == 'v' 
    else 'Divorciado')

print("\nInformações coletadas com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo_descricao}")
print(f"Estado Civil: {estado_civil_descricao}")
