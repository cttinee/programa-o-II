# Desenvolva um sistema de estoque que possui a Classe produtos com as
# seguintes características:
# ○ Atributos: nome, preco, quantidade e codigo.
# ○ Métodos: calcular_total, atualizar_preco e verificar_disponibilidade.

class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"O total para o produto '{self.nome}' (Código: {self.codigo}): R${total:.2f}")
        return total

    def atualizar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
            print(f"O preço do produto '{self.nome}' (Código: {self.codigo}) atualizado para R${self.preco:.2f}")
        else:
            print("O preço não pode ser negativo.")

    def verificar_disponibilidade(self):
        if self.quantidade > 0:
            print(f"O produto '{self.nome}' (Código: {self.codigo}) está disponível em estoque.")
            return True
        else:
            print(f"O produto '{self.nome}' (Código: {self.codigo}) está fora de estoque.")
            return False

produto1 = Produto("Notebook", 3000.00, 10, "NB123")
produto2 = Produto("Mouse", 50.00, 0, "MS456")

produto1.calcular_total()

produto1.atualizar_preco(3200.00)

produto1.verificar_disponibilidade()
produto2.verificar_disponibilidade()