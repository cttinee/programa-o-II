# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
# Escreva um programa que pergunta a situação do usuário (se é idoso, se é gestante, se é PCD ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

prioridade = input("Você é idoso, gestante, PCD ou nenhum destes?"
                "(Digite 'idoso', 'gestante', 'PCD' ou 'nenhum'): ").strip().lower()

if prioridade == 'idoso' or prioridade == 'gestante' or prioridade == 'pcd':
    print("Você pode ter acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")
