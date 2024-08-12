# Suponha que você está desenvolvendo um sistema de biblioteca. 
# Crie a classe Livro com as seguintes características:
# ○ Atributos: titulo, autor, ano_publicacao.
# ○ Métodos: exibir_detalhes.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_detalhes(self):
        detalhes = (f"Título: {self.titulo}\n"
                    f"Autor: {self.autor}\n"
                    f"Ano de Publicação: {self.ano_publicacao}")
        print(detalhes)

livro1 = Livro("Harry Potter", "J. K. Rowling", 1998 - 2007)
livro1.exibir_detalhes()