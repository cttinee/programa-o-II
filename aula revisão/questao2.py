# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra:").upper()
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

if letra in vogais:
   print(f"A letra'{letra}' é uma vogal.")

elif letra in consoantes:
   print(f"A letra'{letra}' é uma consoante.")
else:
   print(f"Letra inválida. Por favor, digite novamente.")