# Escreva um programa que possa cadastrar clientes ou funcionários para uma loja. 
# Se o usuário quiser cadastrar um cliente, dados de nome, endereço, CPF devem ser solicitados. 
# Caso o usuário prefira adicionar um novo funcionário, dados de nome, salário, 
# cargo e CPF devem ser requisitados. Utilize comandos de manipulação de string para personalizar a saída.


def cliente():
    print("Cadastro de cliente")
    nome = input("Nome do cliente: ")
    endereco = input("Endereço do cliente: ")
    cpf = input("CPF do cliente: ")
    
    print("\nCliente cadastrado:")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"CPF: {cpf}")

def funcionario():
    print("Cadastro de funcionário")
    nome = input("Nome do funcionário: ")
    salario = float(input("Salário do funcionário: "))
    cargo = input("Cargo do funcionário: ")
    cpf = input("CPF do cliente: ")

    print("\nFuncionário cadastrado:")
    print(f"Nome: {nome}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Cargo: {cargo}")
    print(f"CPF: {cpf}")

print("Bem-vindo ao sistema de cadastro da nossa loja!")
print("Opções disponíveis:")
print("1 - Cadastrar Cliente")
print("2 - Cadastrar Funcionário")

opcao = int(input("Escolha a opção desejada: "))

if opcao == 1:
    cliente()
elif opcao == 2:
    funcionario()
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
