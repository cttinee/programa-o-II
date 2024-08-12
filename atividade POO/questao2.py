# Crie um sistema para um aplicativo bancário, que possui a Classe
# ContaBancaria com as seguintes características:
# ○ Atributos: titular, saldo, numero_conta e tipo_conta.
# ○ Métodos: depositar, sacar, transferir e verificar_saldo.
# OBS: Após cada alteração no saldo, exiba o novo valor na tela

class contabancaria:
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O depósito de R${valor:.2f} foi realizado com sucesso.")
            self.verificar_saldo()
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"O saque de R${valor:.2f} foi realizado com sucesso.")
                self.verificar_saldo()
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def transferir(self, valor, conta_destino):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                conta_destino.depositar(valor)
                print(f"A transferência de R${valor:.2f} foi realizada com sucesso para a conta {conta_destino.numero_conta}.")
                self.verificar_saldo()
            else:
                print("Saldo insuficiente para a transferência.")
        else:
            print("O valor da transferência deve ser positivo.")

    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")


conta1 = contabancaria("José", 9000.00, "12345-7", "Corrente")
conta2 = contabancaria("Bezerra ", 3000.00, "65432-0", "Poupança")

conta1.depositar(500.00)

conta1.sacar(200.00)

conta1.transferir(1000.00, conta2)